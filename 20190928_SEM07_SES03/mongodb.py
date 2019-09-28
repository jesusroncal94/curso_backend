import pymongo

#Conexion con MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Listado de bases de datos
dbs = myclient.list_database_names()
#Verificacion de existencia de una base de datos
db = "test"
if db in dbs:
    print(f"La base de datos {db} existe")
else:
    print(f"La base de datos {db} no existe")

#Seleccionar una base de datos especifica
mydb = myclient["test"]

#Listado de colecciones
print(mydb.list_collection_names())

#Creacion de una coleccion
nuevacoleccion = mydb["coleccion2"]
print(mydb.list_collection_names())

#Insercion de un documento en la nueva coleccion
diccionario = {"dni": "48082945", "nombre": "Jesus", "apellido": "Roncal"}
nuevacoleccion.insert_one(diccionario)

#Insercion multiple
lista = [{"dni": "87654321", "nombre": "Maria", "apellido": "Roncal"}, {"dni": "12345678", "nombre": "Jose", "apellido": "Roncal"}]
nuevacoleccion.insert_many(lista)

#Muestra de 1 documento de una coleccion
print(mydb.list_collection_names())
print(nuevacoleccion.find_one())
#Muestra de documentos de una coleccion por parámetros de búsqueda
query = {"dni": "48082945"}
documentob = nuevacoleccion.find(query)
for x in documentob:
    print(x)
#Muestra de todos los documentos de una coleccion
documentos = nuevacoleccion.find()
for documento in documentos:
    print(documento)

#Actualizacion de documento (reemplazo)
queryUpdate = {"dni": "48082945"}
nuevacoleccion.update(query, queryUpdate)
documentos = nuevacoleccion.find()
for documento in documentos:
    print(documento)

#Actualizacion de documento indicando campos a actualizar
query = {"dni": "48082945"}
queryUpdate = {"$set": {"nombre": "Jesus E.", "apellido": "Roncal H."}}
nuevacoleccion.update(query, queryUpdate, upsert= True)
documentos = nuevacoleccion.find()
for documento in documentos:
    print(documento)