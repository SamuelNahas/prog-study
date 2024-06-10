linhas, colunas = map(int, input().split())

matriz = [[0] for i in range(colunas)]

for linha in range(linhas):
    for coluna in range(colunas):
        matriz[coluna][linha] = int(input())

for linha in range(linhas):
    for coluna in range(colunas):
        print(matriz[linha][coluna], end=' ')
    print()
