num = int(input())
lista = []

for i in range(num, 0, -1):
    lista.append(i)

lista_result = []
if num % 2 == 0:
    for j in range(len(lista)):
        if lista[j] % 2 != 0:
            lista_result.append(lista[j])
else:
    for k in range(len(lista)):
        if lista[k] % 2 == 0:
            lista_result.append(lista[k])
    lista_result.append(lista[num//2])

print(lista)
print(lista_result)