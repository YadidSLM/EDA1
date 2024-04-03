
#Creabdo diccionarios con dict()

diccionario = dict(nombre = "Yadid", appelido = "Montes", esCool = True)
#Solo se puede hacer diccionarios vacíos con la función dict igual con listas con la función list y tupla con tuple
#diccionario = dict()

diccionario2 = {
        #Key o índice de tipo conjunto (Loquísimo)
        frozenset(["Montes", "Sweet"]): "sup"
}

#Creeando diccionario con fromkeys()
    #Tipo de dato es dict.método
                    #El primer dato son las llaves iterables una llave sería n otra o...,
                    #como las listas son iterables se usan para indicar en cada elemento de la lista la llave
                                #El segundo parámetro es el valor al que se refiere la llave
diccionario3 = dict.fromkeys("nombre", "Valor")
                    #Si no se incluye otro parámetro a parte de la lista las llaves contienen un None o valor vacío
diccionario4 = dict.fromkeys(["parametro1", "parametro2"]) # = dict.fromkeys(["parametro1", "parametro2"], None)
diccionario5 = dict.fromkeys(["parametro1", "parametro2"], "Valor de todas las llaves indicadas en la lista")

print(diccionario3)
print(diccionario4)
print(diccionario5)