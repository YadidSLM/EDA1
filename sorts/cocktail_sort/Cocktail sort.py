def cocktail_sort(array):
    n = len(array)
    swap = True
    start = 0
    end = n-1
    while (swap==True):
        swap = False
        for i in range(start, end):
            if (array[i] > array[i+1]):
                array[i], array[i+1]= array[i+1], array[i]
                swap = True
        if swap == False:
            break

        swap = False
        end = end-1
        
        for i in range(end-1, start-1, -1):
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                swap = True

        start = start+1
        
    return array
    
array = [2, 78, 90, 1, 0, 100]
cocktail_sort(array)
print("Sorted array!", cocktail_sort(array))

    #  i    0   1   2   3   4   5   

    # index 0   1   2   3   4   5
    # data  2   78  90  1   0   100
    # sort  2   78  1   90  0   100
    # sort  2   78  1   0   90  100