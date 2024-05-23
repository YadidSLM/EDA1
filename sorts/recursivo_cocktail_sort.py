#https://pythontutor.com/render.html#mode=display

def cocktailSort(arr, start, tam):
    
    
    end = tam - 1
    if arr[start] < arr[start + 1] and start == end:
        return arr, start
    elif arr[start] > arr[start + 1] and start < end:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    if start < end - 1:
        start += 1
    else:
        return
    cocktailSort(arr, start, tam)
    print(arr)


arr = [4,3,2,1]
cocktailSort(arr, 0, len(arr))


