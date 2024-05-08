def menorValor(num):
    menorValor = 0
    
    for i in range(num):
        valor = int(input())
        if valor < menorValor:
            menorValor = valor
        

    return menorValor

num = int(input())

print(menorValor(num))