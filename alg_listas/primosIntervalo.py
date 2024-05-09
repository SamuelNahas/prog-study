def ehPrimo(num):
    i = 2

    while i < num:
        if num % i == 0:
            return False
        i += 1

    return True


cont = 30

numeroPrimo = 2
while cont <= 1330:
    if ehPrimo(numeroPrimo):
        print(numeroPrimo)
        numeroPrimo += 1
        cont += 1
    else:
        numeroPrimo += 1
    
