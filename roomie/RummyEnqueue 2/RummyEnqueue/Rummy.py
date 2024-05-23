"""

  Rummy versión "Los Enqueue" en python
 
  authors : Pablo Romero, Leonardo Perez, Yadid Montes
  date: 07/04/2024
  subject: EDA1
 
"""

import random
import os
import time
from termcolor import colored
from typing import Literal
import pygame
pygame.init()

if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm-256color'


"""Condiciones globales"""
clave = 0

max_jugadores = 4

num_cartas_NO_comodines = 104
num_comodines = 2
num_colores = 4

suma_inicio = 30
suma_inicio_comodin = suma_inicio/3

colores_comodin = 2
colores_no_comodin = 6
colores_cargados = colores_comodin + colores_no_comodin

num_cartas = num_cartas_NO_comodines + num_comodines

max_cartas_color = int(((num_cartas - num_comodines)/num_colores)/2)

max_mazo = 14
veces_max_cartas_color = 2
cartas_en_pozo = 0

tiempo_espera = 0

jugadores = []  
turnos = []
pozo = []
tablero = []

Cj = []
avatares = ('🐶', '🐺', '🐱', '🦁', '🐯', '🦊', '🦝', '🐮', '🦒', '🐭', '🐹', '🐰', '🐻', '🐸', '👽')
rummy = r"""
  _   ___                            _   ___           _             ___                             
 (_) | _ \ _  _  _ __   _ __   _  _ | | | _ \___ _ _  | |   ___ ___ | __|_ _  __ _ _  _ ___ _  _ ___ 
 | | |   /| || || '  \ | '  \ | || ||_| |  _/ _ \ '_| | |__/ _ (_-< | _|| ' \/ _` | || / -_) || / -_)
 |_| |_|_\ \_,_||_|_|_||_|_|_| \_, |(_) |_| \___/_|   |____\___/__/ |___|_||_\__, |\_,_\___|\_,_\___|
                                 |_/                                            |_|                  
"""

winner = r"""
  _  ___                    _       _ 
 (_)/ __| __ _ _ _  __ _ __| |_ ___| |
 | | (_ |/ _` | ' \/ _` (_-<  _/ -_)_|
 |_|\___|\__,_|_||_\__,_/__/\__\___(_)
"""


class TColores:
    colores: list[Literal['grey', 'white', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']] = [
        'grey',     # Negro (gris oscuro)
        'white',    # Blanco
        'red',      # Rojo
        'green',    # Verde
        'yellow',   # Amarillo
        'blue',     # Azul
        'magenta',  # Rosa
        'cyan',     # Cian
    ]

    colores_rainbow: list[Literal['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']] = [
        'red',      # Rojo
        'green',    # Verde
        'yellow',   # Amarillo
        'blue',     # Azul
        'magenta',  # Rosa
        'cyan',     # Cian
    ]

    def tcolor(texto: str, color: int) -> str:
        # Asegura que el índice esté dentro del rango de colores disponibles
        color_index = color % len(TColores.colores)
        x = TColores.colores[color_index]
        return colored(texto, x, attrs=['bold'])

    def rcolor(texto: str, color: int) -> str:
        # Asegura que el índice esté dentro del rango de colores rainbow disponibles
        color_index = color % len(TColores.colores_rainbow)
        x = TColores.colores_rainbow[color_index]
        return colored(texto, x, attrs=['bold'])

    def rainbow(texto: str) -> str:
        texto_colorido = ""
        for i, char in enumerate(texto):
            if char.strip():  # Solo aplica color si el carácter no está en blanco
                texto_colorido += TColores.rcolor(char, i)
            else:
                texto_colorido += char  # Mantiene los caracteres en blanco sin color
        return texto_colorido


class Cartas:
    def __init__(self, valor, color, posicion_inicial):
        self.valor = valor
        self.color = color
        self.orden = posicion_inicial

    def p_mazo(self, nuevo_orden):
        self.orden = nuevo_orden

    def p_carta(self):
        if self.valor == 0:
            x = "C 🤡"
        else:
            x = self.valor
        print(f"Valor: {x}, Color: {self.color}, Numero visible x ahora xD: {self.orden}\n")

    def carta_archivo(self):
        x = f"${self.valor} /{self.color} @{self.orden}"
        return x


class Player:
    def __init__(self, player_orden, nombre, avatar):
        self.orden = player_orden
        self.nombre = nombre
        self.avatar = avatar
        self.primer_turno = True

    def p_jugador(self):
        x = r_lista(avatares, self.avatar)
        nombre_y_avatar = f"{self.nombre} {x}"
        
        return nombre_y_avatar
    
    def jugador_archivo(self):
        x = f"/{self.orden} ${self.nombre} @{self.avatar}"
        
        return x


"""BOT"""


class Bot(Player):
    def __init__(self, bot_orden, nombre, avatar):
        super().__init__(bot_orden, nombre, avatar)
        self.dificultad = 'difícil'
        self.turno_jugado = 0
        self.primer_turno = True

    def decidir_accion(self, bot_pozo, bot_tablero, mazo_jugador):
        self.turno_jugado += 1
        print(f"Turno {self.turno_jugado} del Bot.")

        accion, detalles = self.considerar_tablero(bot_tablero, mazo_jugador)
        if accion:
            return accion, detalles
        else:
            return self.estrategia_dificil(bot_pozo, mazo_jugador)

    def considerar_tablero(self, bot_dos_tablero, mazo_jugador):
        for indice, jugada in enumerate(bot_dos_tablero):
            for carta in mazo_jugador:
                if carta.valor - 1 in [c.valor for c in jugada] or carta.valor + 1 in [c.valor for c in jugada]:
                    return 'combinar_tablero', (indice, [mazo_jugador.index(carta)])
        return None, None

    def buscar_jugada(self, mazo_jugador):
        valor_contador = {}
        for index, carta in enumerate(mazo_jugador):
            if carta.valor in valor_contador:
                valor_contador[carta.valor].append(index)
            else:
                valor_contador[carta.valor] = [index]

        for indices in valor_contador.values():
            if len(indices) >= 3:
                if self.primer_turno:
                    if sum(mazo_jugador[i].valor for i in indices[:3]) >= suma_inicio:
                        return 'jugar_carta', indices[:3]
                else:
                    return 'jugar_carta', indices[:3]

        color_contador = {}
        for index, carta in enumerate(mazo_jugador):
            if carta.color in color_contador:
                color_contador[carta.color].append(index)
            else:
                color_contador[carta.color] = [index]

        for indices in color_contador.values():
            sorted_indices = sorted(indices, key=lambda x: mazo_jugador[x].valor)
            if len(sorted_indices) >= 3 and all(
                    mazo_jugador[sorted_indices[i]].valor + 1 == mazo_jugador[sorted_indices[i + 1]].valor for i in
                    range(len(sorted_indices) - 1)):
                if self.primer_turno:
                    if sum(mazo_jugador[i].valor for i in sorted_indices[:3]) >= suma_inicio:
                        return 'jugar_carta', sorted_indices[:3]
                else:
                    return 'jugar_carta', sorted_indices[:3]

        return 'tomar_carta', None

    def estrategia_dificil(self, bot_dos_pozo, mazo_jugador):
        accion, indices = self.buscar_jugada(mazo_jugador)
        if accion:
            return accion, indices
        elif len(bot_dos_pozo) > 0:
            return 'tomar_carta', None
        else:
            return 'pasar_turno', None

"""Funciones para evitar crasheos por usuario"""


def int_input_usuario(x):

    while True:
        try:
            numero = int(input(x))
            break 
        except ValueError:
            print("Opción no válida.")

    return numero


def verificar_valores(prompt):
    cadena = input(prompt)
    try:
        valores_enteros = [int(valor) for valor in cadena.split(',')]
        return valores_enteros
    except ValueError:
        print("Opción no válida.")
        return None


def int_lista_comas_usuario(x, max_index):
    while True:
        valores_enteros = verificar_valores(x)
        if valores_enteros is not None:
            if all(0 <= valor <= max_index for valor in valores_enteros):
                return valores_enteros
            else:
                print(f"Los índices deben estar entre 0 y {max_index}.")
        else:
            print("Los índices de las cartas deben estar separados por comas (ej. 0,1):")


"""Funciones de uso comun"""


def mostrar_texto(texto, tiempo):
    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(tiempo / len(texto))
    print("\n")


def reproducir_audio(audio_a_reproducir):
    sonido = pygame.mixer.Sound(f"{audio_a_reproducir}")
    sonido.play()


def generar_aleatorio(x):
    n_random = random.randint(1, x)
    return n_random


def elementos_diferentes(lista):
    
    primer_elemento = lista[0]
    uno_elementos_diferentes = []
    for elemento in lista:
        if elemento != primer_elemento:
            uno_elementos_diferentes.append(elemento)
    
    if len(uno_elementos_diferentes) == 0:
        uno_elementos_diferentes.append(-1)
    
    return uno_elementos_diferentes


def p_lista(lista, columnas):
    for n_elemento, lista in enumerate(lista, 1):
        print(f"{n_elemento}.{lista} ", end='\t')
        if n_elemento % columnas == 0:
            print()


def t_lista(lista):
    while True:
        valor = int_input_usuario("")
        if 1 <= valor <= len(lista):
            return valor - 1
        else:
            print("El valor no se encuentra en la lista")


def r_lista(lista, posicion):
    opcion = int(posicion)
    return lista[opcion - 1]
            

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

def tiempo_x_operacion(tiempo):
    
    time.sleep(tiempo)


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
            if caracter == '.':
                historial_partidas.append(int("".join(t_temp)))
                t_temp.clear()
            elif caracter == " " or caracter == "," or caracter == "\n":
                continue
            else:
                t_temp.append(caracter)

        nombre_partidida = 0

        while True:
            if nombre_partidida in historial_partidas:
                nombre_partidida = nombre_partidida + 1
            else:
                break

    global clave
    clave = nombre_partidida

    historial_partidas.append(clave)

    with open('partidas.txt', 'w') as partidas:
        for elemento in historial_partidas:
            partidas.write(f"{elemento}.\n")


"""Cantidad de jugadores"""


def cant_jugadores():
    
    while True:
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
    
    while c < n_jugadores:
        temp_nombre = input(f"Jugador #{c + 1} ingresa tu nombre: ")
        print(f"{temp_nombre}, escoge tu avatar, estas son las opciones:")
        p_lista(avatares, 5)
        temp_avatar = t_lista(avatares)
        jugadores.append(Player(0, temp_nombre, temp_avatar))
        clean()
        c = c + 1
    
    c = 0
    
    while c < n_jugadores:
        print(f"jugador {c + 1} -> {jugadores[c].p_jugador()}")
        c = c + 1


def datosbot(n_jugadores):
    clean()
    jugadores_humanos = 0
    jugadores_bots = 0

    # Preguntar cantidad de bots
    while True:
        n_bots = int_input_usuario(f"¿Cuántos de los {n_jugadores} jugadores serán bots? (máximo {n_jugadores - 1}): ")
        if 0 <= n_bots <= (n_jugadores - 1):
            break
        else:
            print("Cantidad no válida.")

    # Agregar jugadores humanos
    for c in range(n_jugadores - n_bots):
        temp_nombre = input(f"Jugador #{c + 1} ingresa tu nombre: ")
        print(f"{temp_nombre}, escoge tu avatar, estas son las opciones:")
        p_lista(avatares, 5)
        temp_avatar = t_lista(avatares)
        jugadores.append(Player(c, temp_nombre, temp_avatar))
        clean()
        jugadores_humanos += 1

    # Agregar bots
    c = n_jugadores - n_bots  # Asegurarnos de que 'c' tenga un valor inicial adecuado
    for i in range(n_bots):
        nombre_bot = f"Bot_{i + 1}"
        print(f"Escoge el avatar del {nombre_bot}, estas son las opciones:")
        p_lista(avatares, 5)
        avatar_bot = t_lista(avatares)
        jugadores.append(Bot(c + i, nombre_bot, avatar_bot))
        clean()
        jugadores_bots += 1

    # Mostrar jugadores
    for c in range(n_jugadores):
        print(f"jugador {c + 1} -> {jugadores[c].p_jugador()}")


"""Generar turnos"""


def orden(n_jugadores):
    temp_lista = []

    c = 0
    while c < n_jugadores:
        num_temp = generar_aleatorio(max_cartas_color)
        if num_temp not in temp_lista:
            temp_lista.append(num_temp)
            c = c + 1

    for idx, jugador in enumerate(jugadores):
        jugador.numero = temp_lista[idx]
        print(F"{jugador.p_jugador()} , obtuvo la carta con número {jugador.numero}")

    print("\nOrdenando jugadores por número...")
    # Ordenar la lista de jugadores
    jugadores.sort(key=lambda x: x.numero, reverse=True)

    for idx, jugador in enumerate(jugadores):
        jugador.orden = idx  # Asegurarse de que el orden se refleje en el atributo 'orden'
        print(f"{jugador.p_jugador()}  #{idx + 1}")

    texto_x_tiempo("El orden es...", tiempo_espera)

    # Imprimir
    c = 0
    while c < n_jugadores:
        jugadores[c].orden = c
        print(F"{jugadores[c].p_jugador()}  #{c + 1}")
        c = c + 1
    print()


"""Funciones pila pozo"""


def apilar_pozo(elemento):
       
    global cartas_en_pozo

    pozo.append(elemento)

    cartas_en_pozo = len(pozo) - 1


def desapilar_pozo():
    
    global cartas_en_pozo
    x = cartas_en_pozo

    try:
        ultima_carta = pozo[x]
        cartas_en_pozo = cartas_en_pozo - 1
        pozo.pop()
    except IndexError:
        ultima_carta = "Error"

    return ultima_carta
        

"""Crear cartas"""


def crear_cartas():
    
    numeros_generados = []

    color_origen = 0
    ccolor = 0
    valor = 0
    color = ""
    c = 0
    while c < (max_cartas_color * 2 * num_colores):

        c = c + 1
        valor = valor % max_cartas_color + 1

        if valor == 1:
            color_origen = (color_origen + 1) % veces_max_cartas_color
            if color_origen == 1:
                ccolor = ccolor + 1
                if ccolor == 1:
                    color = 2
                elif ccolor == 2:
                    color = 3
                elif ccolor == 3:
                    color = 4
                elif ccolor == 4:
                    color = 5

                elif ccolor == 5:
                    color = 6
                elif ccolor == 6:
                    color = 74

        while True:
            num_temp = generar_aleatorio(num_cartas)
            if num_temp not in numeros_generados:
                numeros_generados.append(num_temp)
                break

        apilar_pozo(Cartas(valor, color, num_temp))

    valor = 0
    color = ""
    c = 0
    while c < num_comodines:
        
        c = c + 1
        valor = valor % 2 + 1

        if valor == 1:
            color = 0
        elif valor == 2:
            color = 1

        while True:
            num_temp = generar_aleatorio(num_cartas)
            if num_temp not in numeros_generados:
                numeros_generados.append(num_temp)
                break
        
        apilar_pozo(Cartas(0, color, num_temp))
        

"""Ordenar Cartas"""
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


def encolar_mazo(jugador, elemento):

    if elemento == 0:
        print("Pozo vacio")
    else:
        Cj[jugador].append(elemento)


def desencolar_mazo(jugador, pos):

    x = Cj[jugador][pos]

    del Cj[jugador][pos]

    return x


def ordenar_mazo(jugador):
    
    c = 0
    while c < len(Cj[jugador]) - 1:
        cc = c + 1
        while cc < len(Cj[jugador]):
            if Cj[jugador][c].valor > Cj[jugador][cc].valor:
                Cj[jugador][c], Cj[jugador][cc] = Cj[jugador][cc], Cj[jugador][c]
            cc = cc + 1
        c = c + 1


def ordenar_tablero(idx):
    
    c = 0
    while c < len(tablero[idx]) - 1:
        cc = c + 1
        while cc < len(tablero[idx]):
            if tablero[idx][c].valor > tablero[idx][cc].valor:
                tablero[idx][c], tablero[idx][cc] = tablero[idx][cc], tablero[idx][c]
            cc = cc + 1
        c = c + 1


def enumerar_cartas(jugador):

    c = 0

    while c < len(Cj[jugador]):
        Cj[jugador][c].orden = c
        c = c + 1


"""Crear mazo"""


def c_mazo(cant):

    nombre = 0

    while nombre < cant:
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
    while c < tamaniotemp:
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
        if x == 0:
            x = TColores.tcolor("C🤡", int(carta.color))
        else:
            x = TColores.tcolor(f"{carta.valor}", int(carta.color))
        
        lista_val[c].append(x)
        lista_pos[c].append(i)

        cc = cc + 1
        cc = cc % max_cartas_color

        if (cc == 0) and (z != 0):
            c = c + 1
        z = z + 1
        
    c = 0
    while c < tamaniotemp:
        
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
    tamaniotemp = int(tamaniotemp / max_mazo) + 1

    c = 0
    while c < tamaniotemp:
        lista_pos.append([])
        lista_val.append([])
        c += 1

    for i, carta in enumerate(Cj[jugador]):
        if carta.valor == 0:
            texto_carta = TColores.tcolor("C 🤡", carta.color)  # Comodín
        else:
            texto_carta = TColores.tcolor(f"{carta.valor}", carta.color)  # Valor normal

        fila = i // max_mazo
        lista_val[fila].append(texto_carta)
        lista_pos[fila].append(i)

    for i in range(len(lista_val)):
        if lista_val[i]:
            print("Valor:    ", end='\t')
            for elemento in lista_val[i]:
                print(elemento, end="\t")
            print()

            print("Posición:", end='\t')
            for elemento in lista_pos[i]:
                print(elemento, end="\t")
            print("\n")


"""Repartir cartas"""


def r_cartas(n_jugadores):
    
    n_jugador = 0

    while n_jugador < n_jugadores:
        c = 0

        while c < max_mazo:

            carta = desapilar_pozo()

            Cj[n_jugador].append(carta)

            c = c + 1
        
        n_jugador = n_jugador + 1


"""Jugadas"""


def juego_terminado():
    for jugador in range(len(Cj)):
        if len(Cj[jugador]) == 0:
            reproducir_audio("s_victoria.mp3")
            print(f"{jugadores[jugador].p_jugador()} ha ganado!")
            texto_x_tiempo(TColores.rainbow(winner), 1.5 * tiempo_espera)
            print("¡Gracias por jugar!")
            return True
    return False


def es_tercia(cartas):
    if len(cartas) < 3:
        return False
    else:
        # Valores de menor a mayor
        c = 0
        while c < len(cartas) - 1: #Cambiar algoitmo de ordenamineto 
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
            if int(elementos_diff[0]) == -1 or int(elementos_diff[0] == 0):
                return True
        else:
            return False


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
            else:
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
                    else:
                        return False
            else:
                return False
            c = c + 1


def jugar_jugada_independiente(jugador, indices):
    cartas_seleccionadas = [Cj[jugador][i] for i in sorted(indices, reverse=True)]

    puntos_jugada = 0

    for carta in cartas_seleccionadas:
        if carta.valor == 0:
            puntos_jugada += suma_inicio_comodin
        else:
            puntos_jugada += carta.valor

    if jugadores[jugador].primer_turno and puntos_jugada < suma_inicio:
        print(f"La jugada debe sumar al menos {suma_inicio} puntos en el primer turno.")
        return False

    if es_tercia(cartas_seleccionadas) or es_corrida(cartas_seleccionadas):
        agregar_combinacion_al_tablero(cartas_seleccionadas)
        for indice in sorted(indices, reverse=True):
            Cj[jugador].pop(indice)

        jugadores[jugador].primer_turno = False
        return True
    else:
        return False


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


"""Funciones tablero"""


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
                if x == 0:
                    x = TColores.tcolor("C🤡", int(carta.color))
                else:
                    x = TColores.tcolor(f"{carta.valor}", int(carta.color))
                
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


def agregar_combinacion_al_tablero(combinacion):
    global tablero
    tablero.append(combinacion)


def modificar_combinacion_en_tablero(index, nuevas_cartas):
    if 0 <= index < len(tablero):
        tablero[index].extend(nuevas_cartas)
        ordenar_tablero(index)
        print(f"Combinación en índice {index} actualizada.")
        mostrar_tablero()
    else:
        print("Índice de combinación no válido.")


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


def robar_cartas_tablero(jugador):
    cartas_robadas = []
    seguir_robando = True
    while seguir_robando:
        mostrar_tablero()
        idx_jugada = int_input_usuario(
            "Indica el índice de la combinación en el tablero de la cual quieres robar cartas: ") - 1
        if 0 <= idx_jugada < len(tablero):
            if len(tablero[idx_jugada]) > 3:
                print(f"Cartas disponibles en la jugada {idx_jugada + 1}:")

                lista_val = []
                lista_pos = []

                for i, carta in enumerate(tablero[idx_jugada]):
                    x = carta.valor
                    if x == 0:
                        x = TColores.tcolor("C🤡", int(carta.color))
                    else:
                        x = TColores.tcolor(f"{carta.valor}", int(carta.color))

                    lista_val.append(x)
                    lista_pos.append(i)

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

                indices = int_lista_comas_usuario("Indica los índices de las cartas que quieres tomar (ej. 0,1): ",
                                                  len(tablero[idx_jugada]) - 1)

                for i in sorted(indices, reverse=True):
                    if len(tablero[idx_jugada]) - 1 >= 3:
                        carta = tablero[idx_jugada].pop(i)
                        cartas_robadas.append((carta, idx_jugada, i))
                        Cj[jugador].append(carta)
                print("Cartas robadas exitosamente.")
                mostrar_cartas_jugador(jugador)
            else:
                print("No puedes dejar la jugada del tablero con menos de tres cartas o índice inválido.")
        else:
            print("Índice inválido.")

        while True:
            opc = int_input_usuario("¿Deseas robar de otra combinación? \n1) Si\n2) No\n")
            if opc == 1:
                seguir_robando = True
                break
            elif opc == 2:
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


"""Hola"""


def hola():
    reproducir_audio("s_bromita.mp3")
    pr = '''print("Hola mundo =)")
print("Hola python =)")
'''
    texto_x_tiempo(f"{TColores.rainbow(pr)}", tiempo_espera/2)
    input("Presiona Enter para volver...")
    clean()
    

"""Adio"""


def cheems(x):
    cheem = '''⠀⠀⠀⠀⠀ ⣀⣀⣀⣀⡀
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
    texto_x_tiempo(TColores.rainbow(f"{x} \n{cheem}"), tiempo_espera)


"""Ver cartas"""


def ver_cartas():
    crear_cartas()
    mostrar_pozo()
    input("Presiona Enter para volver...")
    clean()


"""Corazón del juego"""


def manejar_turno(jugador_index):
    clean()
    jugador_actual = jugadores[jugador_index]

    if hasattr(jugador_actual, 'p_jugador'):
        if isinstance(jugador_actual, Bot):
            accion, detalles = jugador_actual.decidir_accion(pozo, tablero, Cj[jugador_index])

            if accion == 'jugar_carta':
                if detalles and all(0 <= i < len(Cj[jugador_index]) for i in detalles):
                    if jugar_cartas(jugador_index, detalles):
                        jugadores[jugador_index].primer_turno = False
                    else:
                        if len(pozo) > 0:
                            carta = desapilar_pozo()
                            encolar_mazo(jugador_index, carta)
            elif accion == 'tomar_carta':
                if len(pozo) > 0:
                    carta = desapilar_pozo()
                    encolar_mazo(jugador_index, carta)
            elif accion == 'combinar_tablero':
                if detalles and 0 <= detalles[0] < len(tablero) and all(0 <= i < len(Cj[jugador_index]) for i in detalles[1]):
                    if combinar_con_tablero(jugador_index, detalles[0], detalles[1]):
                        pass
                    else:
                        if len(pozo) > 0:
                            carta = desapilar_pozo()
                            encolar_mazo(jugador_index, carta)
            elif accion == 'pasar_turno':
                if len(pozo) > 0:
                    carta = desapilar_pozo()
                    encolar_mazo(jugador_index, carta)
            time.sleep(tiempo_espera)  # Añadir un pequeño retraso para poder seguir el juego
        else:
            jugada_valida = False
            while not jugada_valida:
                print(f"\nTurno de {jugador_actual.p_jugador()}")
                mostrar_cartas_jugador(jugador_index)
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
                        indices = int_lista_comas_usuario("Indica los índices para tu jugada (ej. 0,1,2): ", len(Cj[jugador_index]) - 1)
                        if jugar_jugada_independiente(jugador_index, indices):
                            jugada_valida = True
                        else:
                            input("Presiona Enter para continuar...")
                    elif eleccion == 2:
                        idx_jugada = int_input_usuario("Indica el índice de la combinación en el tablero a la que deseas agregar cartas: ")
                        indices_cartas = int_lista_comas_usuario("Indica el índice de las cartas que deseas agregar: ", len(Cj[jugador_index]) - 1)
                        if combinar_con_tablero(jugador_index, idx_jugada, indices_cartas):
                            jugada_valida = True
                        else:
                            input("Presiona Enter para continuar...")
                    elif eleccion == 3:
                        if cartas_en_pozo == 0:
                            print("No hay más cartas en el pozo.")
                        else:
                            carta = desapilar_pozo()
                            encolar_mazo(jugador_index, carta)
                            jugada_valida = True
                    elif eleccion == 4:
                        cartas_robadas = robar_cartas_tablero(jugador_index)
                        if cartas_robadas:
                            mostrar_cartas_jugador(jugador_index)
                            print("1) Jugar una jugada independiente")
                            print("2) Combinar con otra jugada en el tablero")
                            eleccion = int_input_usuario("Selecciona una opción (1-2): ")
                            if eleccion == 1:
                                indices = int_lista_comas_usuario("Indica los índices para tu jugada (ej. 0,1,2): ", len(Cj[jugador_index]) - 1)
                                if jugar_jugada_independiente(jugador_index, indices):
                                    jugada_valida = True
                                else:
                                    for carta, idx_jugada, idx_carta in reversed(cartas_robadas):
                                        tablero[idx_jugada].insert(idx_carta, carta)
                                        Cj[jugador_index].remove(carta)
                                    input("Presiona Enter para continuar...")
                                    mostrar_tablero()
                            elif eleccion == 2:
                                idx_jugada = int_input_usuario("Indica el índice de la combinación en el tablero a la que deseas agregar cartas: ")
                                indices_cartas = int_lista_comas_usuario("Indica el índice de las cartas que deseas agregar: ", len(Cj[jugador_index]) - 1)
                                if combinar_con_tablero(jugador_index, idx_jugada, indices_cartas):
                                    jugada_valida = True
                                else:
                                    print("No se pudo agregar las cartas a la jugada. Devolviendo cartas robadas al tablero.")
                                    for carta, idx_jugada, idx_carta in reversed(cartas_robadas):
                                        tablero[idx_jugada].insert(idx_carta, carta)
                                        Cj[jugador_index].remove(carta)
                                    input("Presiona Enter para continuar...")
                                    mostrar_tablero()
                            else:
                                print("Opción no válida, por favor elige 1 o 2.")
                    else:
                        print("Opción no válida, por favor elige 1, 2, 3 o 4.")
                except ValueError:
                    print("Por favor, introduce un número válido.")

                tiempo_x_operacion(tiempo_espera)
                clean()
    else:
        print("Error: El objeto jugador_actual no tiene un método p_jugador()")
    clean()



def juego():
    # Pre Juego
    reproducir_audio("s_juego.mp3")
    mostrar_texto(TColores.rainbow(rummy), 2 * tiempo_espera)
    n_jugadores = cant_jugadores()
    mostrar_texto("Bienvenidos...", tiempo_espera)
    datos(n_jugadores)
    mostrar_texto("Vamos por los turnos...", tiempo_espera)
    clean()
    mostrar_texto("Se repartirán las cartas y los turnos se asignarán a partir de la carta más alta...",
                  3 * tiempo_espera)
    clean()
    mostrar_texto("Revolviendo cartas...", tiempo_espera)
    mostrar_texto("Repartiendo cartas...", tiempo_espera)
    orden(n_jugadores)
    mostrar_texto("¡¡¡Empieza el juego!!!", tiempo_espera)

    # Juego
    clean()
    mostrar_texto("Revolviendo cartas...", tiempo_espera)
    crear_cartas()
    mostrar_texto("Repartiendo cartas...", tiempo_espera)
    ordenar_pozo()
    numero_de_partida()
    mostrar_texto(f"Esta es la partida número {clave}...", tiempo_espera)
    input("Presiona Enter para continuar...")
    c_mazo(n_jugadores)
    r_cartas(n_jugadores)

    mostrar_tablero()

    turno_activo = True
    while turno_activo:
        clean()
        for jugador in range(n_jugadores):
            clean()
            manejar_turno(jugador)
            reproducir_audio("s_turno.wav")
            clean()
            
            if juego_terminado():
                turno_activo = False
                break

    print("El juego ha terminado")
    input("Presiona Enter para continuar...")
    clean()


def juegoBot():
    # Pre Juego
    reproducir_audio("s_juego.mp3")
    mostrar_texto(TColores.rainbow(rummy), 2 * tiempo_espera)
    n_jugadores = cant_jugadores()
    mostrar_texto("Bienvenidos...", tiempo_espera)
    datosbot(n_jugadores)
    mostrar_texto("Vamos por los turnos...", tiempo_espera)
    clean()
    mostrar_texto("Se repartirán las cartas y los turnos se asignarán a partir de la carta más alta...",
                  3 * tiempo_espera)
    clean()
    mostrar_texto("Revolviendo cartas...", tiempo_espera)
    mostrar_texto("Repartiendo cartas...", tiempo_espera)
    orden(n_jugadores)
    mostrar_texto("¡¡¡Empieza el juego!!!", tiempo_espera)

    # Juego
    clean()
    mostrar_texto("Revolviendo cartas...", tiempo_espera)
    crear_cartas()
    mostrar_texto("Repartiendo cartas...", tiempo_espera)
    ordenar_pozo()
    numero_de_partida()
    mostrar_texto(f"Esta es la partida número {clave}...", tiempo_espera)
    input("Presiona Enter para continuar...")
    c_mazo(n_jugadores)
    r_cartas(n_jugadores)

    mostrar_tablero()

    turno_activo = True
    while turno_activo:
        clean()
        for jugador in range(n_jugadores):
            clean()
            manejar_turno(jugador)
            reproducir_audio("s_turno.wav")
            clean()

            if juego_terminado():
                turno_activo = False
                break

    print("El juego ha terminado")
    input("Presiona Enter para continuar...")
    clean()


"""Principal (Este no se mueve sin que los 3 estemos de acuerdo)"""


def main():
    clean()

    menu = '''Menu:
        1)Reglas del juego
        2)Jugar PvP
        3)Jugar vs Bot
        4)Hola
        5)Ver cartas
        6)Salir'''

    while True:

        reproducir_audio("s_inicio.mp3")
        texto_x_tiempo((f"{menu}"), tiempo_espera)
        o = int_input_usuario("")

        if o == 1:
            reglas_de_partida()
        elif o == 2:
            clean()
            juego()
        elif o == 3:
            clean()
            juegoBot()
        elif o == 4:
            clean()
            hola()
        elif o == 5:
            clean()
            ver_cartas()
        elif o == 6:
            clean()
            reproducir_audio("s_final.mp3")
            cheems("Adio =)")
            break
        else:
            print("Opción no valida")


"""Ejecución"""

main()
