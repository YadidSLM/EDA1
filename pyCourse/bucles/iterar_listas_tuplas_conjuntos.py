

animales = ["gato", "perro", "loro", "cocodrilo", "Yep yep"]
numeros = [12, 323, 23, 343 ,2]

for elemento in animales:
    print(f"Ahora la variable elemento es igual a: {elemento}")

#Recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    res = numero * 10
    print(res)

#Iterando ambas con zip, tienen que tener la misma cantidad de elementos
for numero,elemento in zip(animales, numeros):
    print(f"Recorriendo lista animales: {numero}")
    print(f"Recorriendo lista numeros: {elemento}\n")

#De [5, 10) y hace el código dentro del for 5 veces
for i in range(5, 10):
    print(i)

print("\n")

#De 0 a 9 [0, 10)
for i in range(10):
    print(i)

#Froma no óptima de recorrer una lista con su índce (Esto no se puede en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#Forma corrcta de recorrer una lista con su índice
for num in enumerate(numeros):
    #num recorre lo que regresa enumerate que es una tupla del (indice, valor_del_parametro)
    print(f"Indice: {num[0]} y el valor es: {num[1]}")

print("\n")

#Lo mismo que el de arriba, ahora desempaquetando la tupla
for n, i in enumerate(numeros):
    print(f"Indice: {n} y el valor es: {i}")

#Usando for/else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero}")
#Se ejecuta siempre 1 vez lo que hay dentro del else aunque la lista esté vacía
else:
    print("El bucle terminó")


#Todo lo anterior funciona exactamnete igual para tuplas