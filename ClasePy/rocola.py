import numpy as np
import matplotlib.pyplot as plt #Importación absoluta
#import Axes3D.mpltoolkits
from mpl_toolkits.mplot3d import Axes3D #Importación relativa
from playsound import playsound

def main():
    print("     Bienvenido      ")
    print("1. Reproducir música")
    print("2. Graficar un sen x")

    opcion = int(input("Escoge una opción = "))
    
    
    if opcion == 1:
        print("EN CONSTRUCCIÓN")
        print("CANCIONES")
        print("1. AC DC")
        print("2. LED ZEPPILIN")
        print("3. RAMONES")
        print("4. DAFT PUNK")

        band = int(input("Escoge una banda"))
        if band == 1:
            file = ".mp3"
        elif band == 2:
            file = ".mp3"
        elif band == 3:
            file = "heyoh.mp3"
        elif band == 4:
            file = "instant.mp3"
        
        playsound()




    elif opcion == 2:
        x = np.linspace(0, 5, 40)
        fig, ax = plt.subplots(facecolors = 'w', edgecolor = 'k')
        ax.plot(x, sin(x), marker("+", color))

