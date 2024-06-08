linhas = int(input())
matriz = [list(map(int, input().split())) for i in range(linhas)]
colunas = len(matriz[0])

j = 0
for i in range(linhas-1, -1, -1):
    print(matriz[i][j])
    j += 1