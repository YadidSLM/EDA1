"""     Operadores de comparación   """
variable1 = 5 < 4 #Devuelve falso y lo pone en la variable variable1
print(type(variable1)) #Tipo bool

#Comparar usuarios
contraseña_almacendad = "HOla"
contraseña_escrita = "HOla"
print(contraseña_almacendad == contraseña_escrita) #Imprime true o false

"""     Operadores lógicos     """
#Se utiliza & y | para comparar bits, para otras situaciones se utiliza and y or.
#Para la negación se utiliza != como en C

#AND
r1 = True & True    #Devuelve True
r2 = False & True   #Devuelve False
r3 = True & False   #Devuelve False
r4 = False & False  #Devuelve False

#OR

r5 = True | True    #Devuelve True
r6 = False | True   #Devuelve True
r7 = True | False   #Devuelve True
r8 = False | False  #Devuelve False

#NOT

r9 = not True       #Devuelve False
r10 = not False     #Devuelve True

"""     Condicionales   """
planetas = -2

if planetas == 8:
    print("Hay 8 planetas en el sistema solar\n")
elif planetas > 8:

    if planetas > 9:
        print("¿En qué otro planeta estás pensando?")
    else:
        print("Plutón ya no es considerado un planeta del sistema solar.\n")
    
#En C Or se escribe con || doble palito, pero en python es con solo 1 |
elif planetas < 8 or planetas == 0:
    print('''Hay mínimo 8 planetas en el sistema solar.\n''')
else:
    print("Estamos pidiendo un entero no una cadena")

if planetas != -2:
    print("Probando la negación")
elif planetas < 0 and planetas > -10:
    print("El valor está entre -9 y 1")