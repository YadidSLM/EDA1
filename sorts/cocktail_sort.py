import random

def cocktailSort(arr):
    for a in range(len(arr) // 2):
        print(a)
        for i in range(a, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for i in range(len(arr) - (a + 1), 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

arr = [1,2,3,4,5]
random.shuffle(arr)
print(f'{arr}\n')
sorted = cocktailSort(arr)
print(sorted)