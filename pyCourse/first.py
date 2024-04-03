
#Esto es una cadena que se puede asignar a una variable
""" HOla
 que onda
"""
'''
YOooo
How you doing?
'''
"Solo en lína"
'Es lo mismo que la linea de arriba solo que con comillas simples'
#La recomendación de python para nombrar variables es con snake case
num = 5 + 2
num += 2 #Es lo mismo que num = num + 2

#Concaternar con f strings: Convierte en texto cualquier tipo de dato
a_imprimir = f"Numero es {num}"
print(a_imprimir)

#Concatenar con +
saludo = "Hola" + " ¿Cómo se encuentra? El resultado anterior es " + str(num) #Se psa de enetro a cadena
print(saludo)

#Operadores de pertenencia (in / not in)
print("Hola" in saludo) #Devuelven un booleano si se encuentra en el arreglo de caracteres saludo
print("Hola" not in saludo) #Devuelve booleano si no está en cadena saludo

#Para desdeclarar una variable se utiliza del y es como si no se declaró
del a_imprimir