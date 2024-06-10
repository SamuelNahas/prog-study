m, n = map(int, input().split())
matriz = [list(map(int, input().split())) for i in range(m)]
linhas = len(matriz)
colunas = len(matriz[0])
vetor = list(map(int, input().split()))

vetor_resultados = []
for linha in range(linhas):
    somatorio_resultados = 0
    for coluna in range(colunas):
        somatorio_resultados += (matriz[linha][coluna] * vetor[coluna])
    vetor_resultados.append(somatorio_resultados)

print(vetor_resultados)