linhas = int(input())
matriz = [list(map(int, input().split())) for i in range(linhas)]

for i in range(len(matriz)):
    print(matriz[i][i])