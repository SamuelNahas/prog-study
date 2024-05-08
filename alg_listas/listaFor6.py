def maiorValor(num):
    maiorValor = 0
    
    for i in range(num):
        valor = int(input())
        if valor > maiorValor:
            maiorValor = valor

    return maiorValor

num = int(input())

print(maiorValor(num))