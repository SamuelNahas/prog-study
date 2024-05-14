def ehPrimo(num):
    i = 2

    while i < num:
        if num % i == 0:
            return False
        i += 1

    return True


cont = 1

numeroPrimo = 2
while cont <= 50:
    if ehPrimo(numeroPrimo):
        print(-numeroPrimo, end=" ")
        if cont % 10 == 0:
            print()
        numeroPrimo += 1
        cont += 1
    else:
        numeroPrimo += 1
    
