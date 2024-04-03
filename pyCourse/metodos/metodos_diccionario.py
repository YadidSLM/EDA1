dicci = {
    'nombre'   :   "Sebastián",
    'apellido'  :   "Montes",
    'subs'  : 1000
}

#Imprime las claves o índices del diccionario y también sirve para iterar
claves = dicci.keys()

#Devuelve el elemto dentro de la clave o índice ingresado si no lo encuentra devuleve un none, no lanza excepción o error si no lo encuentrs
dentro = dicci.get("nombre")

#Eliminando todo del diccionario
#dicci.clear()

#Eliminando un elemento del diccionario
dicci.pop("subs")

#Obteniendo un elemto dict_items iterable
diccio_iterable = dicci.items()

print(type(diccio_iterable))
print(diccio_iterable)