from clases.conexion import Conexion

class Producto():
    conexion = Conexion()
    con = conexion.conectar()
    
    def __init__(self):
        pass
    
    def mostrarProducto(self):
        sql = 'SELECT * FROM productos'       
        cursor = self.con.cursor()
        cursor.execute(sql)
        productos = cursor.fetchall()
        for producto in productos:
            print(producto)

    def agregarProducto(self, nombreProducto, precioProducto):
        sql = 'INSERT INTO productos(idProducto, nombreProducto, precioProducto) VALUES(%s, %s, %s)'
        valores = (0, nombreProducto, precioProducto)
        cursor = self.con.cursor()
        cursor.execute(sql, valores)
        self.con.commit()
        mensaje = "Producto agregado correctamente"
        return mensaje

    def actualizarProducto(self, idProducto, nombreProducto, precioProducto):
        sql = f"UPDATE productos SET nombreProducto = '{nombreProducto}', precioProducto = '{precioProducto}' WHERE idProducto = '{idProducto}'"
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        mensaje = "Producto actualizado correctamente"
        return mensaje
 
    def eliminarProducto(self, idProducto):
        sql = f"DELETE FROM productos WHERE idProducto = '{idProducto}'"
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        mensaje = "Producto eliminado correctamente"
        return mensaje
    
    def buscarProductoPorCodigo(self, idProducto):
        sql = f'SELECT * FROM productos WHERE idProducto = {idProducto}'
        cursor = self.con.cursor()
        cursor.execute(sql)
        producto = cursor.fetchone()
        return producto