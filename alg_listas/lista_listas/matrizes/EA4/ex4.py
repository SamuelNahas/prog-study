k = int(input())

matriz = []
for i in range(k):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(k):
    for j in range(i+1):
        print(matriz[i][j], end=' ')
    print()
