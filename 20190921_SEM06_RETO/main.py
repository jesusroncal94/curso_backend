from clases.factura import Factura
from clases.producto import Producto

factura = Factura()
factura.guardarFactura()
factura.mostrarFactura()

#CRUD Producto
#Listar y buscar
producto = Producto()
producto.mostrarProducto()

#Actualizar
datos = producto.buscarProductoPorCodigo(2)
idProducto = datos[0]
nombreProducto = "abc"
precioProducto = 5000
producto.actualizarProducto(idProducto, nombreProducto, precioProducto)

#Agregar
nombreProducto = 'Prueba'
precioProducto = 10000
producto.agregarProducto(nombreProducto, precioProducto)

#Eliminar
datos = producto.buscarProductoPorCodigo(7)
idProducto = datos[0]
producto.eliminarProducto(idProducto)

#TAREA PARA CASA :,v
#BUSQUEDA DE FACTURA POR CODIGO (DETALLE)
#CONTROL DE STOCK