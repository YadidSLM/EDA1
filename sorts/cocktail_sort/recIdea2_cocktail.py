import random

# Python program for implementation of Cocktail Sort


def cocktailSort(a):
	n = len(a)
	swapped = True
	start = 0
	end = n-1
	while (swapped == True):
		swapped = False
		for i in range(start, end):
			if (a[i] > a[i + 1]):
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True
		if (swapped == False):
			break
		swapped = False
		end = end-1
		for i in range(end-1, start-1, -1):
			if (a[i] > a[i + 1]):
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True
		start = start + 1


# Driver code 
# a = [3,2,1]
# cocktailSort(a)
# print("Sorted array is:")
# print(a)


# def cocktail_sort(arr, end, begining, increase_or_decrease):
#     for i in range(len(arr) - (a + 1), 0, -1):
#             if arr[i] < arr[i - 1]:
#                 arr[i], arr[i - 1] = arr[i - 1], arr[i]
#     cocktail_sort(arr, len(arr) - (a + 1), 0, -1)



#https://pythontutor.com/render.html#mode=display

def cocktail_sort(arr, start, tam):
    
    
    end = tam - 1
    if arr[start] > arr[start + 1] and start < end:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    if start < end - 1:
        start += 1
    else:
        return
    cocktail_sort(arr, start, tam)
    start -= 1
    if arr[start] > arr[start + 1]:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    start -= 1
    
    print(arr)


arr = [5,43,2,1]
cocktail_sort(arr, 0, len(arr))