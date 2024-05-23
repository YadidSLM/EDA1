"""

  Rummy versión "Los Enqueue" en python
 
  author : Pablo Romero 
  date: 07/04/2024
  subject: EDA1
 
"""

"""Aparado para imports"""
import random
import os
import time

"""Condiciones globales"""
#*** -> significa revisar 
#/// -> quizá se modifica a futuro
clave = 0 #NO BORRAR!!!

max_jugadores = 4

num_cartas_NO_comodines = 104
num_comodines = 2
num_colores = 4 #max 8

num_cartas = num_cartas_NO_comodines + num_comodines



max_cartas_color = int(((num_cartas - num_comodines)/num_colores)/2)

max_mazo = 14
veces_max_cartas_color = 2
cartas_en_pozo = 0 #Este es muy importante para espetar el orden del pozo, NO BORRAR!!!

tiempo_espera = 2 #segundos

#listas
jugadores = []  
turnos = []
pozo = []
tablero = []

#Mazos cartas jugadores (lista doblemete ligada, donde cada elemento es parte de una lsiat circular doblemente ligada)
Cj = []


"""Nomenclaturas en archivo"""

#Jugadores &
    #Orden /
    #Nombre $
    #Avatar @
#Pozo %
    #Cartas:
        #Valor $
        #Color /
            # Lista de colores:
            # 0. rojo
            # 1. verde
            # 2. amarillo
            # 3. azul
            # 4. magenta
            # 5. cyan
            # 6. naranja
            # 7. morado
            # 8. negro
            # 9. blanco
        #Orden @
#Mazos (
#M{njugador}
    #Cartas:
        #Valor $
        #Color /
        #Orden @

avatares = ('🐶','🐺','🐱','🦁','🐯','🦊','🦝','🐮','🦒','🐭','🐹','🐰','🐻','🐸','👽')
rummy = '''\

  _   ___                            _   ___           _             ___                             
 (_) | _ \ _  _  _ __   _ __   _  _ | | | _ \___ _ _  | |   ___ ___ | __|_ _  __ _ _  _ ___ _  _ ___ 
 | | |   /| || || '  \ | '  \ | || ||_| |  _/ _ \ '_| | |__/ _ (_-< | _|| ' \/ _` | || / -_) || / -_)
 |_| |_|_\ \_,_||_|_|_||_|_|_| \_, |(_) |_| \___/_|   |____\___/__/ |___|_||_\__, |\_,_\___|\_,_\___|
                                 |_/                                            |_|                  
'''
winner = '''\
  _  ___                    _       _ 
 (_)/ __| __ _ _ _  __ _ __| |_ ___| |
 | | (_ |/ _` | ' \/ _` (_-<  _/ -_)_|
 |_|\___|\__,_|_||_\__,_/__/\__\___(_)
'''
class T_colores:
    colores = [
        '\033[91m',  # Rojo
        '\033[92m',  # Verde
        '\033[93m',  # Amarillo
        '\033[94m',  # Azul
        '\033[95m',  # Rosa
        '\033[96m',  # Cian
        '\033[38;5;208m',  # Naranja
        '\033[38;5;129m',  # Púrpura
        '\033[30m',   # Negro
        '\033[97m'    # Blanco
    ]
    RESET = '\033[0m'

class cartas:
    def __init__(self, valor, color, orden):
        self.valor = valor
        self.color = color
        self.orden = orden #***

    def p_mazo(self, orden):
        self.orden = orden

    def p_carta(self):
        if (self.valor == 0):
            x = "Comodín 🤡"
        else:
            x = self.valor
        print(f"Valor: {x}, Color: {self.color}, Numero visible x ahora xD: {self.orden}\n")

    def carta_archivo(self):
        x = f"${self.valor} /{self.color} @{self.orden}"
        return(x)

class player:
    def __init__(self, orden, nombre, avatar):
        self.orden = orden
        self.nombre = nombre
        self.avatar = avatar

    def p_jugador(self):
        x = r_Lista(avatares, self.avatar)
        nombre_y_avatar = (f"{self.nombre} {x}")
        
        return (nombre_y_avatar)
    
    def jugador_archivo(self):
        x = f"/{self.orden} ${self.nombre} @{self.avatar}"
        
        return (x)

"""Funciones para evitar crasheos por usuario"""

#Inputs

#Int input
def int_input_usuario(x):

    while True:
        try:
            numero = int(input(x))
            break 
        except ValueError:
            print("Opción no válida.")

    return(numero)

#Verifica si una cadena tiene comas como separadores y son valores enteros
def verificar_valores(x):
    
    cadena = input(x)
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
def int_lista_comas_usuario(x):
    
    while(True):
        valores_enteros = verificar_valores(x)
        if valores_enteros is not None:
            return(valores_enteros)
        else:
            print("Los índices de las cartas deben estar separados por comas (ej. 0,1):")

"""Funciones de uso comun"""

#Texto a color
def T_color(texto, pos_color):
    return T_colores.colores[pos_color % len(T_colores.colores)] + texto + T_colores.RESET

#Texto multicolor
def rainbow(texto):
    letra_x_letra = ""
    c = 0
    while c < len(texto):
        letra_x_letra += T_color(texto[c], c)
        c += 1
    return letra_x_letra

#Numero Aleatorio
def generar_Aleatorio(x):
    n_Random = random.randint(1, x)
    return n_Random
    
#Funciones Lista

#Encontrar elementos diferentes en una lista 
def elementos_diferentes(lista):
    
    primer_elemento = lista[0]
    elementos_diferentes = []
    for elemento in lista:
        if elemento != primer_elemento:
            elementos_diferentes.append(elemento)
    
    if len(elementos_diferentes) == 0:
        elementos_diferentes.append(-1)
    
    return elementos_diferentes

#Imprimir lista enumerada en n columnas
def p_Lista(lista, columnas):
    for n_elemento, lista in enumerate(lista, 1):
        print(f"{n_elemento}.{lista} ",end='\t')
        if n_elemento % columnas == 0:
            print()

#Confirma si el valor entero está en parametro len de la lista             
def t_Lista(lista):
    while(True):
        valor = int_input_usuario("")
        if valor <= len(lista) and valor > 0:
            return valor
            break
        elif valor < 0:
            print("El valor no se encuentra en la lista")
        elif valor > len(lista):
            print("El valor no se encuentra en la lista")

#De numero entero a valor en lista            
def r_Lista(lista, posicion):
    opcion = int(posicion)
    return lista[opcion - 1]
            
#Limpiar Pantalla
def clean():
    if os.name == 'nt':  #Windows
        os.system('cls')
    else:  #Windows'nt
        os.system('clear')
        
#Tiempo entre opereciones
def tiempo_x_operacion(tiempo):
    
    time.sleep(tiempo)

#Texto en tiempo definido 
def texto_x_tiempo(texto, tiempo):
    
    tiempo = tiempo / len(texto)

    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(tiempo)
        
    print("\n")

"""Nombre de partida"""

def numero_de_partida():

    historial_partidas = []
    with open('Partidas.txt', 'r') as t:
        texto = t.read()
        t_temp = []

        for caracter in texto:
            if (caracter == '.'):
                temp_text = "".join(t_temp)
                historial_partidas.append(int(temp_text))
                temp_text = ""
                t_temp.clear()
            elif(caracter == " " or caracter == "," or caracter == "\n"):
                continue
            else:
                t_temp.append(caracter)

        nombre_partidida = 0

        while (True):
            if (nombre_partidida in historial_partidas):
                nombre_partidida = nombre_partidida + 1
            else:
                break

    global clave
    clave = nombre_partidida

    historial_partidas.append(clave)

    with open('partidas.txt', 'w') as partidas:
        for elemento in historial_partidas:
            partidas.write(f"{elemento}.\n")

"""Salvar Partida"""

def salvar_partida():
    with open(f"{clave}.txt", 'w') as archivo:
        #Jugadores
        archivo.write("&\n")
        c = 0
        for elemento in jugadores:
            x = jugadores[c].jugador_archivo()
            archivo.write(f"{x}\n")
            c = c + 1
        #Pozo
        archivo.write("%\n")
        c = 0
        for elemento in pozo:
            x = pozo[c].carta_archivo()
            archivo.write(f"{x}\n")
            c = c + 1
        #Mazos

        c = 0

        while (c < len(Cj)):
            archivo.write(f"({c}\n")
            c1 = 0
            for elemento in Cj[c]:
                x = pozo[c1].carta_archivo()
                archivo.write(f"{x}\n")
                c1 = c1 + 1
            c = c + 1

"""Cantidad de jugadores"""

def cant_Jugadores():
    
    while(True):
        cantidad = int_input_usuario("Ingrese la cantidad de jugadores: ")
        
        if cantidad < 2:
            print("Debe haber al menos 2 jugadores")
        elif cantidad > max_jugadores:
            print(f"Puede haber maximo {max_jugadores} jugadores")
        else:
            print("¡Perfecto!, un poco más y empezamos")
            break
        
    return cantidad

"""Nombre y avatar"""

def datos(n_jugadores):

    clean()
    c = 0
    
    while(c < n_jugadores):
        temp_Nombre = input(f"Jugador #{c + 1} ingresa tu nombre: ")
        print(f"{temp_Nombre}, escoge tu avatar, estas son las opciones:")
        p_Lista(avatares, 5)
        temp_Avatar = t_Lista(avatares)
        jugadores.append(player(0,temp_Nombre,temp_Avatar))
        clean()
        c = c + 1
    
    c = 0
    
    while(c < n_jugadores):
        print(f"jugador {c + 1} -> {jugadores[c].p_jugador()}")
        c = c + 1

"""Generar turnos"""

def orden(n_jugadores):
    
    temp_Lista = []
    
    #Generar numero aleatorio
    c = 0
    while c < n_jugadores:
        num_temp = generar_Aleatorio(max_cartas_color)
        if num_temp not in temp_Lista:
            temp_Lista.append(num_temp)
            c = c + 1

    #Asignar numero aleatorio a el jugador e imprimir
    c = 0
    while c < n_jugadores:
        jugadores[c].numero = temp_Lista[c]
        print(F"{jugadores[c].p_jugador()} , obtuvo la carta con numero {jugadores[c].numero}")
        c = c + 1
    print()

    # Ordenar la lista de jugadores 
    c = 0
    while c < len(jugadores) - 1:
        cc = c + 1
        while cc < len(jugadores):
            if jugadores[c].numero < jugadores[cc].numero:
                jugadores[c], jugadores[cc] = jugadores[cc], jugadores[c]
            cc = cc + 1
        c = c + 1
    
    texto_x_tiempo("El orden es...", tiempo_espera)
    
    #Imprimir
    c = 0
    while c < n_jugadores:
        jugadores[c].orden = c
        print(F"{jugadores[c].p_jugador()}  #{c + 1}")
        c = c + 1
    print()

"""Funciones pila pozo"""

#Apilar
def apilar_pozo(elemento):
       
    global cartas_en_pozo

    pozo.append(elemento)

    cartas_en_pozo = len(pozo) - 1

#Desapilar

def desapilar_pozo():
    
    global cartas_en_pozo
    x = cartas_en_pozo

    #Se obtiene el valor de la carta para almacenarlo en el mazo de cada jugador
    try:
        ultima_carta = pozo[x]
        #Se elimina la carta del pozo
        cartas_en_pozo = cartas_en_pozo - 1
        pozo.pop()
    except IndexError:
        ultima_carta = "Error"

    return(ultima_carta)
        
"""Crear cartas"""

def crear_cartas():
    
    numeros_generados = []
    
    #asignar valores a las cartas y almacenarlas en lista
    
    Ccolor_Origen = 0
    Ccolor = 0
    valor = 0
    color = ""
    c = 0
    while (c < (max_cartas_color * 2 * num_colores)):
        
        #asignar valor a la carta
        c = c + 1
        valor = (valor) % max_cartas_color + 1
        
        #asignar color  
        
        if (valor == 1):
            Ccolor_Origen = (Ccolor_Origen + 1) % veces_max_cartas_color
            if (Ccolor_Origen == 1):
                Ccolor = Ccolor + 1
                if (Ccolor == 1):
                    color = 0
                elif (Ccolor == 2):
                    color = 1
                elif (Ccolor == 3):
                    color = 2
                elif (Ccolor == 4):
                    color = 3
                    
                #por si piden mas colores de carta
            
                elif (Ccolor == 5):
                    color = 4
                elif (Ccolor == 6):
                    color = 5
                elif (Ccolor == 7):
                    color = 6
                elif (Ccolor == 8):
                    color = 7
            
        #asignar numero aleatorio a la carta
        while (True):
            num_temp = generar_Aleatorio(num_cartas)
            if (num_temp not in numeros_generados):
                numeros_generados.append(num_temp)
                break
        
        #apilar en pozo
        apilar_pozo(cartas(valor,color,num_temp))
        
    #asignar valores a los comodines y almacenarlas en lista

    valor = 0
    color = ""
    c = 0
    while (c < num_comodines):
        
        c = c + 1
        valor = ((valor) % 2) + 1
        
        #asignar color  
        
        if (valor == 1):
            color = 8
        elif (valor == 2):
            color = 9
        
        #asignar numero aleatorio a la carta
        while (True):
            num_temp = generar_Aleatorio(num_cartas)
            if (num_temp not in numeros_generados):
                numeros_generados.append(num_temp)
                break
        
        apilar_pozo(cartas(0,color,num_temp))
        
"""Ordenar Cartas""" #(Aquí se simula el revolver cartas)
"""Revolver cartas y guardarlas en pila"""

def ordenar_pozo():
    
    c = 0
    while c < len(pozo) - 1:
        cc = c + 1
        while cc < len(pozo):
            if pozo[c].orden > pozo[cc].orden:
                pozo[c], pozo[cc] = pozo[cc], pozo[c]
            cc = cc + 1
        c = c + 1

""""Funciones cola mazos"""

#Enqueue XD

def encolar_mazo(jugador, elemento):

    if (elemento == 0):
        print("Pozo vacio")
    else:
        Cj[jugador].append(elemento)

#Desencolar

def desencolar_mazo(jugador, pos):

    x = Cj[jugador][pos]

    del Cj[jugador][pos]

    return(x)

#Ordenar mazo

def ordenar_mazo(jugador):
    
    c = 0
    while c < len(Cj[jugador]) - 1:
        cc = c + 1
        while cc < len(Cj[jugador]):
            if Cj[jugador][c].valor > Cj[jugador][cc].valor:
                Cj[jugador][c], Cj[jugador][cc] = Cj[jugador][cc], Cj[jugador][c]
            cc = cc + 1
        c = c + 1

#Ordenar tablero

def ordenar_tablero(idx):
    
    c = 0
    while c < len(tablero[idx]) - 1:
        cc = c + 1
        while cc < len(tablero[idx]):
            if tablero[idx][c].valor > tablero[idx][cc].valor:
                tablero[idx][c], tablero[idx][cc] = tablero[idx][cc], tablero[idx][c]
            cc = cc + 1
        c = c + 1

#Enumerar cartas

def enumerar_cartas(jugador):

    c = 0

    while (c < len(Cj[jugador])):
        Cj[jugador][c].orden = c
        c = c + 1

"""Crear mazo"""

def c_mazo(cant):

    nombre = 0

    while (nombre < cant):
        temp = f"{nombre}" 
        temp = []
        Cj.append(temp)

        nombre = nombre + 1

"""Imprimir pozo"""    

def mostrar_pozo():
    print(f"\nCartas en pozo {len(pozo)}:\n")
    print(f"\nCartas por cada color {max_cartas_color}:\n")

    lista_pos = []
    lista_val = []

    tamaniotemp = len(pozo)
    tamaniotemp = int(tamaniotemp/max_cartas_color) + 1

    c = 0
    while (c < tamaniotemp):
        lista_pos.append(c)
        lista_pos[c] = []
        lista_val.append(c)
        lista_val[c] = []
        c = c + 1
    
    c = 0
    z = 0
    cc = 0

    for i, carta in enumerate(pozo):
        x = carta.valor
        if (x == 0):
            x = T_color("C🤡", int(carta.color))
        else:
            x = T_color(f"{carta.valor}", int(carta.color))
        
        lista_val[c].append(x)
        lista_pos[c].append(i)

        cc = cc + 1
        cc = (cc)%max_cartas_color

        if ((cc == 0) and (z != 0)):
            c = c + 1
        z = z + 1
        
    c = 0
    while (c < tamaniotemp):
        
        if len(lista_val[c]) != 0:
            print("Valor:    ", end='\t')
        for elemento in lista_val[c]:
            print(elemento, end="\t")
        
        if len(lista_val[c]) != 0:
            print()

        if len(lista_pos[c]) != 0:
            print("Posición:", end='\t')
        for elemento in lista_pos[c]:
            print(elemento, end="\t")

        if len(lista_pos[c]) != 0:
            print("\n")
        print()
        c = c + 1

"""Imprimir mazo de cada jugador"""    

def mostrar_cartas_jugador(jugador):
    print(f"\nMazo de {jugadores[jugador].p_jugador()}:")

    lista_pos = []
    lista_val = []

    tamaniotemp = len(Cj[jugador])
    tamaniotemp = int(tamaniotemp/max_mazo) + 1

    c = 0
    while (c < tamaniotemp):
        lista_pos.append(c)
        lista_pos[c] = []
        lista_val.append(c)
        lista_val[c] = []
        c = c + 1
    
    c = 0
    z = 0
    cc = 0

    for i, carta in enumerate(Cj[jugador]):
        x = carta.valor
        if (x == 0):
            x = T_color("C🤡", int(carta.color))
        else:
            x = T_color(f"{carta.valor}", int(carta.color))
        
        lista_val[c].append(x)
        lista_pos[c].append(i)

        cc = cc + 1
        cc = (cc)%max_mazo

        if ((cc == 0) and (z != 0)):
            c = c + 1
        z = z + 1
        
    c = 0
    while (c < tamaniotemp):
        
        if len(lista_val[c]) != 0:
            print("Valor:    ", end='\t')
        for elemento in lista_val[c]:
            print(elemento, end="\t")
        
        if len(lista_val[c]) != 0:
            print()

        if len(lista_pos[c]) != 0:
            print("Posición:", end='\t')
        for elemento in lista_pos[c]:
            print(elemento, end="\t")

        if len(lista_pos[c]) != 0:
            print("\n")

        c = c + 1

"""Repartir cartas"""

def r_cartas(n_jugadores):
    
    n_jugador = 0

    while (n_jugador < n_jugadores):
        c = 0

        while (c < max_mazo):
            
            #Se obtiene el valor de la carta para almacenarlo en el mazo de cada jugador
            carta = desapilar_pozo()
            
            #Asignación de cartas al jugador
            Cj[n_jugador].append(carta)

            c = c + 1
        
        n_jugador = n_jugador + 1

"""Jugadas"""

#Condición de juego terminado NO BORRAR!!!
def juego_terminado():
    for jugador in range(len(Cj)):
        if len(Cj[jugador]) == 0:
            print(f"{jugadores[jugador].p_jugador()} ha ganado!")
            texto_x_tiempo(rainbow(winner), 1.5 * tiempo_espera)
            print("¡Gracias por jugar!")
            return True
    return False

#Tercia con comodín (vector comodín)
def es_tercia(cartas):
    if (len(cartas) < 3):
        return False
    else:
        # Valores de menor a mayor
        c = 0
        while c < len(cartas) - 1:
            cc = c + 1
            while cc < len(cartas):
                if cartas[c].valor < cartas[cc].valor:
                    cartas[c], cartas[cc] = cartas[cc], cartas[c]
                cc = cc + 1
            c = c + 1

        # Crea una lista con los valores de las cartas ordenadas
        c = 0
        cartas1 = []
        while c < len(cartas):
            cartas1.append(cartas[c].valor)
            c = c + 1

        elementos_diff = elementos_diferentes(cartas1)

        # Comprueba si los valores son iguales, ignorando 0 como comodín
        if len(elementos_diff) == 1:
            if (int(elementos_diff[0]) == -1 or int(elementos_diff[0]) == 0):
                return True
        else:
            return False

#Corrida con comodín (vector comodín)
def es_corrida(cartas):

    # Ordena las cartas de menor a mayor
    c = 0
    while c < len(cartas) - 1:
        cc = c + 1
        while cc < len(cartas):
            if cartas[c].valor > cartas[cc].valor:
                cartas[c], cartas[cc] = cartas[cc], cartas[c]
            cc = cc + 1
        c = c + 1
    
    # Crea una lista con los valores de las cartas ordenadas
    c = 0
    cartas1 = []
    while c < len(cartas):
        cartas1.append(cartas[c].valor)
        c = c + 1

    # Comprueba si los valores son consecutivos, ignorando 0 como comodín
    if cartas1[0] == 0:
        if cartas1[1] == 0:
            print("Solo se puede usar un comodín a la vez")
            return False
        else:
            c = 1
            z = 0
            while c < len(cartas1) - 1:
                cc = c + 1 
                if cartas1[cc] == cartas1[c] + 1:
                    c = c + 1
                elif (cartas1[cc] == cartas1[c] + 2) and (z < 1):
                    c = c + 1
                    z = z + 1
                elif cartas1[cc] != cartas1[c] + 1:
                    return False

            cartas2 = []
            while c < len(cartas):
                cartas2.append(cartas[c].color)
                c = c + 1    

            elementos_diff = elementos_diferentes(cartas2)

            if (int(elementos_diff[0]) == 8) or (int(elementos_diff[0]) == 9) or (int(elementos_diff[0]) == -1):
                return True
            else :
                return False
                
    else:
        c = 0
        while c < len(cartas1) - 1:
            cc = c + 1 
            if cartas1[cc] == cartas1[c] + 1:
                if c == len(cartas1) - 2:
                    cartas2 = []
                    while c < len(cartas):
                        cartas2.append(cartas[c].color)
                        c = c + 1    

                    elementos_diff = elementos_diferentes(cartas2)

                    if (int(elementos_diff[0]) == 8) or (int(elementos_diff[0]) == 9) or (int(elementos_diff[0]) == -1):
                        return True
                    else :
                        return False
            else:
                return False
            c = c + 1

#Comprobación tercia o corrida 
def jugar_jugada_independiente(jugador, indices):
    cartas_seleccionadas = [Cj[jugador][i] for i in sorted(indices, reverse=True)]
    if es_tercia(cartas_seleccionadas) or es_corrida(cartas_seleccionadas):
        agregar_combinacion_al_tablero(cartas_seleccionadas)
        for indice in sorted(indices, reverse=True):
            Cj[jugador].pop(indice)
        return True
    else:
        return False

#Función general de manejo de jugadas
def jugar_cartas(jugador, indices):
    cartas_seleccionadas = [Cj[jugador][i] for i in sorted(indices, reverse=True)]

    if es_tercia(cartas_seleccionadas) or es_corrida(cartas_seleccionadas):
        agregar_combinacion_al_tablero(cartas_seleccionadas)

        for indice in sorted(indices, reverse=True):
            Cj[jugador].pop(indice)

        print("Jugada realizada con éxito y añadida al tablero.")
        return True
    else:
        print("Jugada no válida. Intenta de nuevo.")
        return False

"""Funciones tablero""" #(Lista simplemente ligada donde cada elemento es una cola doblemente ligada)

#Imprimir tablero
def mostrar_tablero():
    if not tablero:
        print("El tablero está vacío.")
    else:
        lista_pos = []
        lista_val = []

        print("Combinaciones en el Tablero:")
        for i, combinacion in enumerate(tablero):
            print(f"Combinación {i + 1}:")
            
            lista_pos.append(i)
            lista_pos[i] = []
            lista_val.append(i)
            lista_val[i] = []

            cc = 0

            for carta in combinacion:
                x = carta.valor
                if (x == 0):
                    x = T_color("C🤡", int(carta.color))
                else:
                    x = T_color(f"{carta.valor}", int(carta.color))
                
                lista_val[i].append(x)
                lista_pos[i].append(cc)

                cc = cc + 1

            if len(lista_val[i]) != 0:
                print("Valor:    ", end='\t')
            for elemento in lista_val[i]:
                print(elemento, end="\t")
                    
            if len(lista_val[i]) != 0:
                print()

            if len(lista_pos[i]) != 0:
                print("Posición:", end='\t')
            for elemento in lista_pos[i]:
                print(elemento, end="\t")

            if len(lista_pos[i]) != 0:
                print("\n")

#Agregar combinacion al tablero despues de jugada individual ... Enlistar? 
def agregar_combinacion_al_tablero(combinacion):
    global tablero
    tablero.append(combinacion)

#Modificar combinacion EXISTENTE en el tablero
def modificar_combinacion_en_tablero(index, nuevas_cartas):
    if 0 <= index < len(tablero):
        tablero[index].extend(nuevas_cartas)
        ordenar_tablero(index)
        print(f"Combinación en índice {index} actualizada.")
        mostrar_tablero()
    else:
        print("Índice de combinación no válido.")

#Agregar cartas a combinación EXISTENTE en el tablero
def combinar_con_tablero(jugador, idx_jugada, indices_cartas):
    idx_jugada -= 1
    if 0 <= idx_jugada < len(tablero):
        jugada_original = tablero[idx_jugada][:]

        cartas_a_agregar = [Cj[jugador][i] for i in indices_cartas]
        nueva_jugada = jugada_original + cartas_a_agregar

        if es_tercia(nueva_jugada) or es_corrida(nueva_jugada):
            tablero[idx_jugada].extend(cartas_a_agregar) 
            ordenar_tablero(idx_jugada)  
            for indice in sorted(indices_cartas, reverse=True):
                Cj[jugador].pop(indice)
            return True
        else:
            print("La combinación de cartas no forma una jugada válida.")
    else:
        print("Índice de jugada inválido.")
    return False

#Tomar una carta de una combinacion EXISTENTE en el tablero y agregarla al maso del jugador ... Desenlistar?
def robar_cartas_tablero(jugador):
    cartas_robadas = []
    seguir_robando = True
    while seguir_robando:
        mostrar_tablero()
        idx_jugada = int_input_usuario("Indica el índice de la jugada en el tablero de la cual quieres robar cartas: ") - 1
        if 0 <= idx_jugada < len(tablero) and len(tablero[idx_jugada]) > 3:
            print(f"Cartas disponibles en la jugada {idx_jugada + 1}:")

            lista_val = []
            lista_pos = []    

            cc = 0

            for i, carta in enumerate(tablero[idx_jugada]):

                x = carta.valor
                if (x == 0):
                    x = T_color("C🤡", int(carta.color))
                else:
                    x = T_color(f"{carta.valor}", int(carta.color))
                
                lista_val.append(x)
                lista_pos.append(cc)

                cc = cc + 1

            if len(lista_val) != 0:
                print("Valor:    ", end='\t')
            for elemento in lista_val:
                print(elemento, end="\t")
                    
            if len(lista_val) != 0:
                print()

            if len(lista_pos) != 0:
                print("Posición:", end='\t')
            for elemento in lista_pos:
                print(elemento, end="\t")

            if len(lista_pos) != 0:
                print("\n")

            indices = int_lista_comas_usuario("Indica los índices de las cartas que quieres tomar (ej. 0,1): ")
            
            for i in sorted(indices, reverse=True):
                if len(tablero[idx_jugada]) - 1 >= 3:
                    carta = tablero[idx_jugada].pop(i)
                    cartas_robadas.append((carta, idx_jugada, i))
                    Cj[jugador].append(carta)
            print("Cartas robadas exitosamente.")
            mostrar_cartas_jugador(jugador)
        else:
            print("No puedes dejar la jugada del tablero con menos de tres cartas o índice inválido.")

        while(True):
            opc = int_input_usuario("¿Deseas robar de otra combinación? \n1) Si\n2) No\n")
            if (opc == 1):
                seguir_robando = True
                break
            elif (opc == 2):
                seguir_robando = False
                break
            else:
                print("Opción no valida")
    return cartas_robadas

"""Reglas del juego"""

def reglas_de_partida():
    
    clean()
    with open('Reglas.txt', 'r') as r:
        reglas = r.read()

    texto_x_tiempo(f"{reglas}\n", 5*tiempo_espera)
    input("Presiona Enter para volver...")
    clean()

"""Hola""" #Bromita XD

def hola():
    pr = '''print("Hola mundo =)")
print("Hola python =)")
'''
    texto_x_tiempo(f"{rainbow(pr)}", tiempo_espera/2)
    input("Presiona Enter para volver...")
    clean()
    
"""Adio"""

def cheems(x):
    cheems = '''⠀⠀⠀⠀⠀ ⣀⣀⣀⣀⡀
⠀⠀⠀⠀⡀⣯⡭⠀⢟⢿⣷⣄
⠀⠀⠀⢠⣼⠏⠴⠶⠈⠘⠻⣘⡆
⠀⠀⣠⣾⡟⠁⡀⠀⠀⠀⡼⠡⠛⡄
⠀⠀⠙⠻⢴⠞⠁⠀⠊⠀⠀⠀⠈⠉⢄
⠀⠀⠀⠀⢀⠀⠀⠀⢃⠄⠂⠀⠀⢀⠞⢣⡀
⠀⠀⠀⠀⡌⠁⠀⠀⠀⢀⠀⠐⠈⠀⠀⡺⠙⡄
⠀⠀⠀⠀⡿⡀⠀⠀⠀⠁⠀⠴⠁⠀⠚⠀⡸⣷
⠀⠀⠀⠀⢹⠈⠀⠀⠀⠀⠔⠁⠀⢀⠄⠀⠁⢻⣧
⠀⠀⠀⠀⣸⠀⢠⣇⠀⢘⣬⠀⠀⣬⣠⣦⣼⣿⠏
⡠⠐⢂⡡⠾⢀⡾⠋⠉⠉⡇⠀⢸⣿⣿⣿⡿⠃
⠉⢉⡠⢰⠃⠸⠓⠒⠂⠤⡇⠀⡿⠟⠛⠁
⠘⢳⡞⣅⡰⠁⠀⠀⠀⢀⠇⠀⡇
⠀⠀⠉⠉⠀⠀⠀⠀⢀⣌⢀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠘⠊'''
    texto_x_tiempo(rainbow(f"{x} \n{cheems}"), tiempo_espera)

"""Ver cartas"""
def ver_cartas():
    crear_cartas()
    mostrar_pozo()
    input("Presiona Enter para volver...")
    clean()

"""Corazón del juego""" #Logica jugadas y opciones
def manejar_turno(jugador):
    clean()
    jugada_valida = False
    
    while not jugada_valida:
        
        print(f"\nTurno de {jugadores[jugador].p_jugador()}")
        mostrar_cartas_jugador(jugador)
        print("\nEstado actual del tablero:")
        mostrar_tablero()

        print("\nElige una acción:")
        print("1) Jugar una jugada individual (tercia o corrida)")
        print("2) Agregar a una jugada en el tablero")
        print("3) Tomar una carta del pozo")
        print("4) Robar carta(s) de una o más jugadas en el tablero y jugar")

        eleccion = int_input_usuario("Selecciona una opción (1-4): ")

        try:
            
            eleccion = int(eleccion)
            if eleccion == 1:
                indices = int_lista_comas_usuario("Indica los índices para tu jugada (ej. 0,1,2): ")
                if jugar_jugada_independiente(jugador, indices):
                    print("Jugada realizada con éxito.")
                    jugada_valida = True
                else:
                    print("Jugada no válida. Intenta de nuevo.")
                    input("Presiona Enter para continuar...")
            elif eleccion == 2:
                while (True):
                                idx_jugada = int_input_usuario("Indica el índice de la jugada en el tablero a la que deseas agregar cartas: ")
                                if idx_jugada <= len(tablero):
                                    break
                                else:
                                    print("Opción no válida.")
                
                indices_cartas = int_lista_comas_usuario("Indica el índice de la jugada en el tablero a la que deseas agregar cartas: ")
                if combinar_con_tablero(jugador, idx_jugada, indices_cartas):
                    print("Cartas agregadas con éxito a la jugada.")
                    jugada_valida = True
                else:
                    print("No se pudo agregar las cartas a la jugada.")
                    input("Presiona Enter para continuar...")
            elif eleccion == 3:
                if cartas_en_pozo == 0:
                    print("No hay mas cartas en el pozo.")
                    
                    while(True):
                        eleccion1 = int_input_usuario("Presiona 1 para volver o 2 para pasar...")
                        if eleccion1 == 1:
                            break
                        elif eleccion1 == 2:
                            jugada_valida = True
                            break
                        else:
                            print("Opción no valida")
                else:
                    carta = desapilar_pozo()
                    encolar_mazo(jugador,carta)
                    x = carta.valor
                    if (x == 0):
                        x = T_color("C🤡", int(carta.color))
                    else:
                        x = T_color(f"{carta.valor}", int(carta.color))
                    print(f"Tomaste la carta {x} del pozo")
                    jugada_valida = True
            elif eleccion == 4:
                clean()
                cartas_robadas = robar_cartas_tablero(jugador)
                clean()
                if cartas_robadas:
                    mostrar_tablero()
                    print("Ahora debes jugar con las cartas robadas.")
                    mostrar_cartas_jugador(jugador)
                    print("\nElige una acción:")
                    print("1) Jugar una jugada individual (tercia o corrida)")
                    print("2) Agregar a una jugada en el tablero")

                    try:
                        
                        eleccion = int_input_usuario("Selecciona una opción (1-2): ")
                        if eleccion == 1:
                            indices = int_lista_comas_usuario("Indica los índices para tu jugada (ej. 0,1,2): ")
                            if jugar_jugada_independiente(jugador, indices):
                                print("Jugada realizada con éxito.")
                                jugada_valida = True
                            else:
                                print("Jugada no válida. Devolviendo cartas robadas al tablero.")
                                for carta, idx_jugada, idx_carta in reversed(cartas_robadas):
                                    tablero[idx_jugada].insert(idx_carta, carta)
                                    Cj[jugador].remove(carta)
                                input("Presiona Enter para continuar...")
                                mostrar_tablero()
                        elif eleccion == 2:
                            while (True):
                                idx_jugada = int_input_usuario("Indica el índice de la jugada en el tablero a la que deseas agregar cartas: ")
                                if idx_jugada <= len(tablero):
                                    break
                                else:
                                    print("Opción no válida.")

                            indices_cartas = int_lista_comas_usuario("Indica el índice de la jugada en el tablero a la que deseas agregar cartas: ")
                            if combinar_con_tablero(jugador, idx_jugada, indices_cartas):
                                print("Cartas agregadas con éxito a la jugada.")
                                jugada_valida = True
                            else:
                                print("Jugada no válida. Devolviendo cartas robadas al tablero.")
                                for carta, idx_jugada, idx_carta in reversed(cartas_robadas):
                                    tablero[idx_jugada].insert(idx_carta, carta)
                                    Cj[jugador].remove(carta)
                                input("Presiona Enter para continuar...")
                                mostrar_tablero()
                        else:
                            print("Por favor, introduce un número válido.")
                    except ValueError:
                        print("Jugada no válida. Devolviendo cartas robadas al tablero.")
                        for carta, idx_jugada, idx_carta in reversed(cartas_robadas):
                            tablero[idx_jugada].insert(idx_carta, carta)
                            Cj[jugador].remove(carta)
                        input("Presiona Enter para continuar...")
                        mostrar_tablero()
            else:
                print("Opción no válida, por favor elige 1, 2, 3 o 4.")
        except ValueError:
            print("Por favor, introduce un número válido.")

        tiempo_x_operacion(tiempo_espera)
        clean()
    clean()

def juego():
    # Pre Juego
    texto_x_tiempo(rainbow(rummy), 2 * tiempo_espera)
    n_jugadores = cant_Jugadores()
    texto_x_tiempo("Bienvenidos...", tiempo_espera)
    datos(n_jugadores)
    texto_x_tiempo("Vamos por los turnos...", tiempo_espera)
    clean()
    texto_x_tiempo("Se repartirán las cartas y los turnos se asignarán a partir de la carta más alta...",
                   3 * tiempo_espera)
    clean()
    texto_x_tiempo("Revolviendo cartas...", tiempo_espera)
    texto_x_tiempo("Repartiendo cartas...", tiempo_espera)
    orden(n_jugadores)
    texto_x_tiempo("¡¡¡Empieza el juego!!!", tiempo_espera)

    # Juego
    clean()
    texto_x_tiempo("Revolviendo cartas...", tiempo_espera)
    crear_cartas()
    texto_x_tiempo("Repartiendo cartas...", tiempo_espera)
    ordenar_pozo()
    #numero_de_partida()
    #salvar_partida()
    texto_x_tiempo(f"Esta es la partida número {clave}...", tiempo_espera)
    input("Presiona Enter para continuar...")
    c_mazo(n_jugadores)
    r_cartas(n_jugadores)
    #salvar_partida()

    mostrar_tablero()

    #Cola circular bucle infinito jugadores
    turno_activo = True
    while turno_activo:
        clean()
        for jugador in range(n_jugadores):
            clean()
            manejar_turno(jugador)
            clean()
            if juego_terminado():
                turno_activo = False
                break
            
    print("El juego ha terminado")
    input("Presiona Enter para continuar...")
    clean()

"""Principal (Este no se mueve sin que los 3 estemos de acuerdo)"""

def main():

    print(max_cartas_color)
    menu = '''Menu ***Temporal***
        1)Reglas del juego
        2)Cargar Partida***por ahora no disponible
        3)Jugar
        4)Hola
        5)Ver cartas
        6)Salir'''
    
    while (True):

        o = int_input_usuario(f"{menu}\n")

        if (o == 1):
            reglas_de_partida()
        elif (o == 2):
            break
        elif (o == 3):
            clean()
            juego()
        elif (o == 4):
            clean()
            hola()
        elif (o == 5):
            clean()
            ver_cartas()
        elif (o == 6):
            cheems("Adio =)")
            break
        else:
            print("Opción no valida")

"""Ejecución"""

main()