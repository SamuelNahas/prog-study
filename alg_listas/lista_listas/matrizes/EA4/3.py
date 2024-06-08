matriz = [list(map(int, input().split())) for i in range(int(input()))]
linhas = len(matriz)
colunas = len(matriz)

maior = 0
for linha in range(linhas):
    for coluna in range(colunas):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            posicao_maior = [linha, coluna]
            
print("O maior elemento da matriz é {0} e se encontra na linha {1} e coluna {2}".format(maior, posicao_maior[0]+1, posicao_maior[1]+1))