lista = list(map(int, input().split()))
m = int(input())
ultimo = len(lista)-1

for i in range(len(lista)):
    if lista[i] == m:
        lista[i] = lista[ultimo]
        lista.pop()
        break

print(lista)