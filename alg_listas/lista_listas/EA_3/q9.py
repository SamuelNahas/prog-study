lista = list(map(int, input().split()))
elemento = int(input())
flag = 0
tam = len(lista)
for i in range(tam):
    if lista[i] >= elemento:
        indice_insercao = i 
        flag = 1
        break

if flag:
    lista.append(-1)
    for j in range(tam, indice_insercao, -1):
        lista[j] = lista[j-1]
    lista[indice_insercao] = elemento
    print(lista)
else:
    lista.append(elemento)
    print(lista)