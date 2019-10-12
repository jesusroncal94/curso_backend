from clases.conexion import Conexion
from clases.producto import Producto
from datetime import date

class Factura():
    conexion = Conexion()
    con = conexion.conectar()
    
    def __init__(self):
        pass

    def guardarFactura(self):
        #OBTENER EL ULTIMO ID DE FACTURA
        ultimoID = 0        
        sql = 'SELECT COUNT(*) FROM facturas'
        cursor = self.con.cursor()
        cursor.execute(sql)
        dato = cursor.fetchone()
        ultimoID = dato[0]
        cursor.close()
        idFactura = ultimoID + 1
        #INICIO DE FACTURA
        print(f'FACTURA N° {idFactura}')
        fechaFactura = date.today()
        #OBTENER EL SUBTOTAL DE LA FACTURA
        subtotalFactura = self.guardarDetalle(idFactura)
        igvFactura = subtotalFactura / 1.18
        totalFactura = subtotalFactura + igvFactura
        sql = 'INSERT INTO facturas(idFactura, fechaFactura, subtotalFactura, igvFactura, totalFactura) VALUES(%s, %s, %s, %s, %s)'
        facturas = (0, fechaFactura, subtotalFactura, igvFactura, totalFactura)
        cursor = self.con.cursor()
        cursor.execute(sql, facturas)
        self.con.commit()
        cursor.close()
        return

    def guardarDetalle(self, idFactura):
        numeroProductos = int(input('¿Cuántos productos agregará en la factura?: '))
        print('***LISTA PRODUCTOS***')
        producto = Producto()
        producto.mostrarProducto()
        subtotal = 0
        for i in range(1, numeroProductos + 1):
            idProducto = input(f'ID Producto {str(i)}: ')
            cantidadProducto = float(input(f'Cantidad producto {str(i)}: '))
            productoEncontrado = producto.buscarProductoPorCodigo(idProducto)
            precioProducto = float(productoEncontrado[2])
            subtotal += cantidadProducto * precioProducto
            sql = 'INSERT INTO detalles(idDetalle, idFactura, idProducto, cantidadProducto) VALUES(%s, %s, %s, %s)'
            detalles = (0, idFactura, idProducto, cantidadProducto)
            cursor = self.con.cursor()
            cursor.execute(sql, detalles)
            self.con.commit()
        cursor.close()
        return subtotal

    def mostrarFactura(self):
        sql = 'SELECT * FROM facturas'
        cursor = self.con.cursor()
        cursor.execute(sql)
        facturas = cursor.fetchall()
        print('***REPORTE DE FACTURAS***')
        print('N°, FECHA, SUBTOTAL, IGV, TOTAL')
        for factura in facturas:
            print(f'{factura[0]}, {factura[1]}, {factura[2]}, {factura[3]}, {factura[4]}')
        cursor.close()