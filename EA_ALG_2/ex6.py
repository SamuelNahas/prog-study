n = int(input())
cont = 1
maiorValor = 0
valores = []

while cont <= n:
    valor = int(input())

    if valor > maiorValor:
        maiorValor = valor
    cont += 1


print(maiorValor)
