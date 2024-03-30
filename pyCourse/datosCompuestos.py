#Listas, se ingresan a ellas por su índice
lista = ["Lucas", "Estado: Feliz", True, 1.70, 34, "Sí"]
print(lista[1])

#Tuplas, son similares a las listas solo que no se puede modificar y se usan paréntesis
ej_tupla = ("yoo", 2, 3.23, "Gol", False)
#ej_tupla[1] = 1 Esto da error
ej_tupla = ("Se modificó", 2)
print(ej_tupla[1])

#Conjuntos (set)
conjunto = {1, "Fango", True, 2.64345, 1}
#print[0] = 3 Error! No se accede a elemtos por índice, se puede accedar a elemtos con un bucle
print(conjunto) #No almacena elemetos repetidos

#Diccionario
dictionary = {
#   Índice  : dato
    "id"    : "321073077",
    'nombre': "Yadid", #No importa si es comilla simple o doble
    'edad'  : 18,
    "cool"  : True
}
print(dictionary["id"])
print(dictionary['id'])
print(dictionary['nombre'])
