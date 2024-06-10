matriz = [list(map(int, input().split())) for i in range(int(input()))]
# matriz = [[1, 5, 6, 7], [2, 3, 4, 2], [4, 5, 6, 6], [6, 8, 9, 10]]
# prog_coluna = [0][0, 1, 2, 3] -> [1][1, 2, 3] -> [2][2, 3] -> [3][3]
# prog_linha = [0, 1, 2, 3]
linhas = len(matriz)
colunas = len(matriz[0])
space = ''
for linha in range(linhas):
    print(space, end='')
    for coluna in range(linha, linhas):
        print(matriz[linha][coluna], end=' ')
    space += '  '
    print()