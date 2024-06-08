linhas = int(input())
matriz = [list(map(int, input().split())) for i in range(linhas)]
colunas = len(matriz[0])

indice = linhas
for linha in range(linhas):
    for coluna in range(indice):
        print(matriz[linha][coluna], end=' ')
    indice -= 1
    print()
        