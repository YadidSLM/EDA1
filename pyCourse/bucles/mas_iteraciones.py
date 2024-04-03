stuff = ["pen", "pencil", "desk", "apple", "pinaple", "piginlecacho"]
cadena = 'Hola'
bit_coins = [2, 4, 6, 10]
#Avoiding taking fruits, it doesn't take into account the apple and pinaple elemnents
for cosa in stuff:
    if cosa == "apple" or cosa == 'pinaple':
        continue
    print(f'I\'m gonna take the {cosa} ')

#Avoids the loop to keep iterating, else doesn't run as well
for cosa in stuff:
    if cosa == "piginlecacho":
        break
    print(cosa)
else:
    print("Done")

#For in more than 1 line
doubled_coins = list() #Empty list
for number in bit_coins:
    doubled_coins.append(number * 2)
print(doubled_coins)

#For in just one line
doubled_coins2 = [num * 2 for num in bit_coins]
print(doubled_coins2)

#While is just the same as in C
cont = 0
while cont < 6:
    print(stuff[cont])
    cont += 1


#Normal function
def multi(x):
    return x * 2
#Lambda function of noraml function

#mult_by_two is a function which returned value is x * 2 and its entered parameter is x
mult_by_two = lambda x : x * 2

print(mult_by_two(3))
print(multi(3))