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
max_jugadores = 4
max_cartas = 106
max_cartas_color = 13
num_comodines = 2
max_mazo = 14
veces_max_cartas_color = 2
cartas_en_pozo = 0 #Este es muy importante para espetar el orden del pozo, NO BORRAR!!!

tiempo_espera = 3 #segundos

#listas
jugadores = []
turnos = []

#Mazos cartas jugadores
Cj1 = []
Cj2 = []
Cj3 = []
Cj4 = []
pozo = []


avatares = ('🐶','🐺','🐱','🦁','🐯','🦊','🦝','🐮','🦒','🐭','🐹','🐰','🐻','🐸','👽')
rummy = '''\
  _   ___                            _   ___           _             ___                             
 (_) | _ \ _  _  _ __   _ __   _  _ | | | _ \___ _ _  | |   ___ ___ | __|_ _  __ _ _  _ ___ _  _ ___ 
 | | |   /| || || '  \ | '  \ | || ||_| |  _/ _ \ '_| | |__/ _ (_-< | _|| ' \/ _` | || / -_) || / -_)
 |_| |_|_\ \_,_||_|_|_||_|_|_| \_, |(_) |_| \___/_|   |____\___/__/ |___|_||_\__, |\_,_\___|\_,_\___|
                                 |_/                                            |_|                  
'''

class cartas:
    def __init__(self, valor, color, orden):
        self.valor = valor
        self.color = color
        self.orden = orden #***

    def p_carta(self):
        print(f"Valor: {self.valor} \nColor: {self.color}\nNumero visible x ahora xD: {self.orden}\n")

class player:
    def __init__(self, numero, nombre, avatar,):
        self.numero = numero
        self.nombre = nombre
        self.avatar = avatar
        
    def p_Jugador(self):
        
        nombre_y_avatar = (f"{self.nombre} {self.avatar}")
        
        return (nombre_y_avatar)

"""Funciones de uso comun"""

#Numero Aleatorio
def generar_Aleatorio(x):
    n_Random = random.randint(1, x)
    return n_Random
    
#Funciones Lista

#Imprimir lista enumerada en n columnas
def p_Lista(lista, columnas):
    for n_elemento, lista in enumerate(lista, 1):
        print(f"{n_elemento}.{lista} ",end='\t')
        if n_elemento % columnas == 0:
            print()

#Confirma si el valor entero está en parametro len de la lista             
def t_Lista(lista):
    while(True):
        valor = int(input())
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

#Texto en tiempo definido 
def texto_x_tiempo(texto, tiempo):
    
    tiempo = tiempo / len(texto)

    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(tiempo)
        
    print("\n")

"""Cantidad de jugadores"""

def cant_Jugadores():
    
    while(True):
        cantidad = int(input("Ingrese la cantidad de jugadores: "))
        
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
        temp_Avatar = r_Lista(avatares, temp_Avatar)
        jugadores.append(player(0,temp_Nombre,temp_Avatar))
        clean()
        c = c + 1
    
    c = 0
    
    while(c < n_jugadores):
        print(f"jugador {c + 1} -> {jugadores[c].p_Jugador()}")
        c = c + 1

"""Generar turnos"""

def orden(n_jugadores):
    
    clean()
    
    texto_x_tiempo("Se repartirán las cartas y los turnos se asiganarán a partir de la carta mas alta...", 3*tiempo_espera)
    clean()
    
    texto_x_tiempo("Revolviendo cartas...", tiempo_espera)
    texto_x_tiempo("Repartiendo cartas...", tiempo_espera)
    
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
        print(F"{jugadores[c].p_Jugador()} , obtuvo la carta con numero {jugadores[c].numero}")
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
        print(F"{jugadores[c].p_Jugador()}  #{c + 1}")
        c = c + 1
    print()
        
"""Crear cartas"""

def crear_cartas():
    
    numeros_generados = []
    
    #asignar valores a las cartas y almacenarlas en lista
    
    Ccolor_Origen = 0
    Ccolor = 0
    valor = 0
    color = ""
    c = 0
    while (c < max_cartas - num_comodines):
        
        #asignar valor a la carta
        c = c + 1
        valor = (valor) % max_cartas_color + 1
        
        #asignar color  
        
        if (valor == 1):
            Ccolor_Origen = (Ccolor_Origen + 1) % veces_max_cartas_color
            if (Ccolor_Origen == 1):
                Ccolor = Ccolor + 1
                if (Ccolor == 1):
                    color = "Rojo"
                elif (Ccolor == 2):
                    color = "Azul"
                elif (Ccolor == 3):
                    color = "Verde"
                elif (Ccolor == 4):
                    color = "Amarillo"
                    
                #por si piden mas colores de carta
            
                elif (Ccolor == 5):
                    color = "Naranja"
                elif (Ccolor == 6):
                    color = "Rosa"
                elif (Ccolor == 7):
                    color = "Morado"
                elif (Ccolor == 8):
                    color = "Blanco"
                elif (Ccolor == 7):
                    color = "Negro"    
            
        #asignar numero aleatorio a la carta
        while (True):
            num_temp = generar_Aleatorio(max_cartas)
            if (num_temp not in numeros_generados):
                numeros_generados.append(num_temp)
                break
        
        pozo.append(cartas(valor,color,num_temp))
        
    #asignar valores a los comodines y almacenarlas en lista

    valor = 0
    color = ""
    c = 0
    while (c < num_comodines):
        
        c = c + 1
        valor = (valor) % num_comodines + 1
        
        #asignar color  
        
        if (valor == 1):
            color = "Blanco"
        elif (valor == 2):
            color = "Negro"
                            
        #por si piden mas colores de comodines
        
        elif (valor == 3):
            color = "Verde"
        elif (valor == 4):
            color = "Amarillo"
        elif (valor == 5):
            color = "Naranja"
        elif (valor == 6):
            color = "Rosa"
        elif (valor == 7):
            color = "Morado"
        elif (valor == 8):
            color = "Rojo"
        elif (valor == 7):
            color = "Azul"    
        
        #asignar numero aleatorio a la carta
        while (True):
            num_temp = generar_Aleatorio(max_cartas)
            if (num_temp not in numeros_generados):
                numeros_generados.append(num_temp)
                break
        
        pozo.append(cartas("Comodín 🤡",color,num_temp))
    
    global cartas_en_pozo
    cartas_en_pozo = len(pozo) - 1
        
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

"""Repartir cartas"""

def r_cartas(n_jugadores):
    
    c_jugador = 0
    c = 0
    cj_mazo = 0
    global cartas_en_pozo
    
    while (cj_mazo < n_jugadores):
        
        #Se obtiene el valor de la carta para almacenarlo en el mazo de cada jugador
        temp_carta = pozo[cartas_en_pozo]
        cartas_en_pozo = cartas_en_pozo - 1
        
        c = c % max_mazo + 1
        
        #Contadores para salir del bucle
        if (c == 1):
            c_jugador = c_jugador + 1
            
        if (c == max_mazo):
            cj_mazo = cj_mazo + 1
        
        #Asignación de cartas al jugador
        if (c_jugador == 1):
            Cj1.append(temp_carta)
        elif (c_jugador == 2):
            Cj2.append(temp_carta)
        elif (c_jugador == 3):
            Cj3.append(temp_carta)
        elif (c_jugador == 4):
            Cj4.append(temp_carta)
            
        #Se elimina la carta del pozo
        pozo.pop()

"""Imprimir mazo de cada jugador"""    

def p_mazo(jugador):
    
    c = 0
    while (c < max_mazo):
        if (jugador == 0):
            print(f"Mazo Jugador {jugadores[jugador].p_Jugador()}")
            Cj1[c].p_carta()
        elif (jugador == 1):
            print(f"Mazo Jugador {jugadores[jugador].p_Jugador()}")
            Cj2[c].p_carta()
        elif (jugador == 2):
            print(f"Mazo Jugador {jugadores[jugador].p_Jugador()}")
            Cj3[c].p_carta()
        elif (jugador == 3):
            print(f"Mazo Jugador {jugadores[jugador].p_Jugador()}")
            Cj4[c].p_carta()
        
        c = c + 1

"""Principal (Este no se mueve sin que los 3 estemos de acuerdo)"""

def main():
    
    #Pre Juego
    texto_x_tiempo(rummy, 2*tiempo_espera)
    n_jugadores = cant_Jugadores()
    texto_x_tiempo("Bienvenidos...", tiempo_espera)
    datos(n_jugadores)
    texto_x_tiempo("Vamos por los turnos...", tiempo_espera)
    orden(n_jugadores)
    texto_x_tiempo("¡¡¡Empieza el juego!!!", tiempo_espera)
    
    #Juego
    clean()
    texto_x_tiempo("Revolviendo cartas...", tiempo_espera)
    crear_cartas()
    texto_x_tiempo("Repartiendo cartas...", tiempo_espera)
    ordenar_pozo()
    r_cartas(n_jugadores)
    
    #Esto servirá para control por el momento
    p_mazo(0)
    p_mazo(1)
    print("Por el momento se ve, pero luego ya no XD")
    
"""Ejecución"""

main()