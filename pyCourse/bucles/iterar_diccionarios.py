diccionario = dict(nombre = "Yadid", apellido = "López", edad = 18)
print(diccionario)

#Recorriendo un diccionario para obtener las clavez
for indice in diccionario:
    print(f"Clave o índice es \"{indice}\"")


print("\n")

#Recorreindo un diccionario con items() para obtener las claves y los valores
# diccionario.items() devuelve una tupla el primer elemeto es el índice y el segundo es el valor
for indice, dato in diccionario.items():
    print(f"Clave o índice es \"{indice}\" y su valor es \"{dato}\"")