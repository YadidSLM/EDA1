import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np

#Para medir las iteraciones en ambos algoritmos de ordenamiento se utiliza i_times y n_times
i_times = 0
def cocktailSort(arr):
    global i_times
    for a in range(len(arr) // 2):
        for i in range(a, len(arr) - 1):
            i_times += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for i in range(len(arr) - (a + 1), 0, -1):
            i_times += 1
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

n_times = 0
def cocktail_sort_recursivo(arr, start, tam):
    global n_times
    end = tam - 1
    n_times += 1
    if arr[start] > arr[start + 1] and start < end:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    if start < end - 1:
        start += 1
    else:
        return arr
    cocktail_sort_recursivo(arr, start, tam)
    n_times += 1
    start -= 1
    if arr[start] > arr[start + 1]:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    start -= 1
    if start == -1:
        start = 1
    return arr

def ordenamineto_cocktel_recursivo(arr):
    global n_times
    for a in range((len(arr) // 2)):
        cocktail_sort_recursivo(arr, 0, len(arr))
        n_times += 1
    return arr


TAM = 500
eje_x = list(range(1,TAM,1))
eje_y = []
eje_y2 = []
lista_variable = []

for num in eje_x:
    lista_is = random.sample(range(0,10000), num)
    lista_qs = lista_is
    lista_variable, times = (ordenamineto_cocktel_recursivo(lista_is), n_times)
    cocktailSort(lista_qs)
    eje_y.append(times)
    eje_y2.append(i_times)

    

# Funciones Big - O
x = range(1,TAM,1)
y = [10*_ for _ in x]
y_cuadrada = [i*2 for i in x]
y_nlogn = x * np.log(x)
y_logn = np.log(x)


fig, ax = plt.subplots(facecolor = 'w', edgecolor = 'k')
#Funciones
ax.plot(eje_x, eje_y, marker = 'o', color = 'g', linestyle = '-')
ax.plot(eje_x, eje_y2, marker = 'o', color = 'b', linestyle = 'None')
ax.plot(eje_x, y_cuadrada, color = 'r')
ax.plot(eje_x, y_nlogn, color = 'b')
ax.plot(eje_x, y_logn, color = 'y')

ax.set_xlabel('x')
ax.set_ylabel('y')
#Escala logarítmica
ax.set_yscale('log')
ax.grid(True)
ax.legend(['Cocktail Sort Recursivo', 'Cocktail Sort', 'O(x^2)'])

plt.title('Cocktail sort recursivo y no recursivo')
plt.show()