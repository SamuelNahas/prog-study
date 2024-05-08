def ehPrimo(num):
    cont = 0
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


num = int(input())

if ehPrimo(num):
    print("O número {0} é primo".format(num))
else:
    print("O número {0} não é primo".format(num))