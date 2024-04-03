conjunto = set(["Dato1", "Dato2"])
print(conjunto)

#Para meter un conjunto dentro de una localidad de otro conjunto se usa frozenset
#frozenset crea un conjunto, a prtir de una lista, inmutable (que no se puede modificar)
conjunto1 = frozenset(["asdfg", 13])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#Teoría de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}
conjunto3 = {6, 2, 9, 2, 4}

#Devuelve booleano si es subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Devuelve booleano si es superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto1 > conjunto2

#Devuelve True si no hay un resultado en común si es disjoint
resultado = conjunto1.isdisjoint(conjunto3)


print(resultado)