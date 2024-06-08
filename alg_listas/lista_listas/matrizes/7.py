matriz = [list(map(int, input().split())) for i in range(int(input()))]
colunas = len(matriz[0])
linhas = len(matriz)

for linha in range(linhas):
    for coluna in range(linha+1):
        print(matriz[linha][coluna], end='*')
    print()