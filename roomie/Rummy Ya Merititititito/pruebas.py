#Verifica si una cadena tiene comas como separadores y son valores enteros
def verificar_valores():
    
    cadena = input("Indica los índices de las cartas que quieres tomar (ej. 0,1):")
    if ',' not in cadena:
        try:
            valores_enteros = [int(valor) for valor in cadena.split(',')]
            return valores_enteros
        except ValueError:
            print("Opción no válida.")
            return None
    else:
        if ',' in cadena:
            try:
                valores_enteros = [int(valor) for valor in cadena.split(',')]
                return valores_enteros
            except ValueError:
                print("Opción no válida.")
                return None
        else:
            print("Opción no válida.")
            return None

#Ciclo hasta que "verificar_valores" se cumpla 
def int_lista_comas_usuario():
    
    while(True):
        valores_enteros = verificar_valores()
        if valores_enteros is not None:
            return(valores_enteros)
        else:
            print("Los índices de las cartas deben estar separados por comas (ej. 0,1):")

x = int_lista_comas_usuario()
print(x)