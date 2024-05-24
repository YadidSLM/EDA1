# #https://pythontutor.com/render.html#mode=display
import random
def cocktail_sort_recursivo(arr, start, tam):
    
    #for a in range(len(arr) // 2):
    end = tam - 1
    if arr[start] > arr[start + 1] and start < end:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    if start < end - 1:
        start += 1
    else:
        return
    cocktail_sort_recursivo(arr, start, tam)    
    start -= 1
    if arr[start] > arr[start + 1]:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    start -= 1
    if start == -1:
        start = 1
    return arr

def ordenamineto_cocktel(arr):
    for a in range((len(arr) // 2)):
        cocktail_sort_recursivo(arr, 0, len(arr))
    return arr

arr = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(arr)
print(f'{arr}\n')
print(ordenamineto_cocktel(arr))
