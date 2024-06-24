def regresar_prios(n):
    primos = [1,2]
    while n > 2:
        if n % 2 != 0:
            if n > 9:
                if n % 3 != 0 and n % 4 != 0 and n % 5 != 0 and n % 6 != 0 and n % 7 != 0 and n % 8 != 0 and n % 9 != 0:
                    primos.append(n)
            else:
                if n == 3 or n == 5 or n == 7:
                    primos.append(n)
        n = n - 1
    return primos
n = input("Numeros primos: ")
print(regresar_prios(int(n)))