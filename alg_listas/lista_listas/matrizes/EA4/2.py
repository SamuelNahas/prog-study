matriz = [list(map(int, input().split())) for i in range(int(input()))]
linhas = len(matriz)
colunas = len(matriz)

maior = 0
for linha in range(linhas):
    for coluna in range(colunas):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]

print(maior)