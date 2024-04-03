#Creando una lista con lis()
#               0       1      2    3   4        5                
lista = list(["Hola", True, 3.1342, 7, True, "Love you"])
#              -6      -5     -4   -3  -2       -1
lista2 = list([1, 4, True, -1, 2, 1, 1, False])

#Devuelve la cantidad de elementos de la lista
elemet_amount = len(lista)

#Agregando un elemento a la lista
lista.append("Sup")

#Agregando un elemto a la lista por un índice específico
lista.insert(3, "Insertado")

#Agregando varios elementos a la lista
lista.extend(["Nuevo", 23, True])

#Eliminando un elemto de la lista por su índice

lista.pop(2) #Al quitar un elemto se recorren los demás y así no deja huecos
lista.pop(-10) #-1 para eliminar el último elemento, -2 para el antepenúltimo y así sucesivamente
#print(lista)

#Removiendo un elemnto de la lista por su valor
lista.remove("Insertado")

#Eliminando todos los elementos de la lista
#lista.clear()

#Ordena la lista acdente (Si usamos el parámetro reverse=True lo ordena en reversa)
    #La lista no debe incluir cadenas
print(lista2)
lista2.sort()

#Invirtiendo los elementos de una lista sin ordenarla y pueden tener cadenas
lista.reverse()


print(lista)

