lista = list(map(int, input().split()))
elemento = int(input())
tam = len(lista)

indice_elemento = 0
flag = 0
for i in range(tam):
    if lista[i] == elemento:
        indice_elemento = i 
        flag = 1
        break
        
if flag:
    for j in range(indice_elemento, tam-1):
        lista[j] = lista[j+1]       
    lista.pop()
    print(lista)
else:
    print("O elemento não existe na lista")