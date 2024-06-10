matriz = [list(map(int, input().split())) for i in range(int(input()))]
colunas = len(matriz[0])
linhas = len(matriz)

for coluna in range(colunas):
    for linha in range(coluna, -1, -1):
        print(matriz[linha][coluna], end=' ')
    print()