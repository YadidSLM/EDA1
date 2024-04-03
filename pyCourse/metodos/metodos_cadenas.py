# Estrucurta de un método: DATO.METODO()

cadena1 = "I love Jesus"
cadena2 = "Amo a Jesús"
cadenaN = "198765"
cadenaAN = "abcdefghijklmnñopqrstuvwxyz"
#print(dir("hey")) #Muestra las funciones y métodos del tipo de dato de lo que hay dentro del paréntesis

#   Convertir a minúsculas
min = cadena1.lower()
#   Convertir a mayúsculas
mayu = cadena1.upper()
#   Primera letra en mayúscula lo demás en minúsculas
cap = cadena1.capitalize()

#   Buzca una cadena en otra cadena y devuelve el índice donde se encuntra
    #Si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("J")
#   Buzca una cadena en otra cadena y devuelve el índice donde se encuntra
    #Si no hay coincidencia lanza una exepción que es como un error
busqueda_index = cadena1.index("l")

#Checa si en la cadena hay caracteres numéricos
is_numeric = cadenaN.isnumeric()
#Checa si en la cadena son alfanumercios es decir de la a a la z en cualquier orden
is_alpha = cadenaAN.isalpha()

#Devuelve la cantidad de coincidencias de una cadena dentro de otra cadena
contar_coincidencias = cadena1.count("lo")
#Devuelve cuántos carcateres tiene una cadena
numC = len(cadenaAN)

#Devuelve booleano si una cadena empieza con otra cadena dada
empieza_con = cadena1.startswith("I love")

#Devuelve booleano si una cadena termina con otra cadena dada
termina_con = cadena1.endswith("s")

#Si el valor 1 se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
    #si no se encuentra devuelve la cadena original
new_string = cadena1.replace("I", "You")

#Separar cadenas con la cadena que le pasemos y devuelve una lista con los elementos separados
cadena_separada = cadena1.split(" ")

print(type(cadena_separada))
print(cadena_separada)