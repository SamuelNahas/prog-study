matriz = [list(map(int, input().split())) for i in range(int(input()))]
linhas = len(matriz)
colunas = len(matriz)

linha = int(input())-1

maior = 0
for coluna in range(colunas):
    if matriz[linha][coluna] > maior:
        maior = matriz[linha][coluna]

print("O maior elemento da linha {0} é: {1}".format(linha-1, maior))