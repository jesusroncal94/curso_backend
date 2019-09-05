lista = [1,2,3,4]
lista.append(5)
print(lista)

lista2 = ["a", "b", "c"]
lista.extend(lista2)
print(lista)

lista.insert(2, 6)
print(lista)

lista.remove(6)
print(lista)

print(lista.index(6))

lista.pop(0)
print(lista)

print(len(lista))

print(lista.count)

#Ejercicio
personas = ["Jorge", "Juan", "Carlos", 4, 5, 6]
print(personas)
personas.append("Dexter")
print(personas)
i = personas.index("Juan")
print("Juan está en la posición: ", i)
j = personas.index(5)
print("5 está en la posición: ", j)
personas.remove("Carlos")
print(personas)

nota = int(input("Ingrese su nota: "))
if nota >= 14:
    print("Aprobaste!")
else:
    print("Desaprobaste!")

iteracion = 0
numero = 1
suma = 0
print("Valores iniciales")
print("Iteracion: ", iteracion)
print("Numero es: ", numero)
print("Suma es: ", numero)
while numero <= 10:
    iteracion += 1
    suma += numero
    numero += 1
    print(suma, end=', ')
print("Valores finales")
print("Iteracion: ", iteracion)
print("Numero es: ", numero)
print("Suma es: ", suma)

palabras = ["gato", "ventana", "defenestrado"]
for p in palabras:
    print(palabras.index(p), end=': ')
    print(p, end=', ')
for i, p in enumerate(palabras):
    print(i, p, end=': ')

for i in range(0, 10, 2):
    print(i, end=', ')

palabras = ['gato', 'perro', 'ventana', 'defenestrado']
for p in palabras:
    if p == "ventana":
        break
    print(p)

#Ejercicio
listado = [1, 3, 20, 10, 50, 100, 31, 1000]
for x in listado:
    if x == 3:
        print(x)
for x in listado:
    if x % 2 == 0:
        print(x, " es par!")
for x in listado:
    print(x)
    if x == 50:
        break
"""
Tarea:
- Ingresar 2 Valores
- Escoger operacion signo o por texto
Archivos:
1. los valores de las variables
2. validar los datos y los signos u operacion
3. llamar funcion
Enviar al chat
"""