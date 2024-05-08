n = int(input())
cont = 1

while cont <= n:
    valor = int(input())
    
    if cont == 1:
        menor_valor = valor + 1

    if valor < menor_valor:
        menor_valor = valor
    cont += 1


print(menor_valor)
