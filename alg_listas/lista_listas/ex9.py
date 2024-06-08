# Tentando descobrir se um dado é viciado, um jogador o lançou n vezes. 
# Dados os n resultados do lançamento, determine o número de ocorrências de cada face.


n = int(input())


ocorrencias = [0, 0, 0, 0, 0, 0]

for i in range(n):
    lancamento = int(input())
    
    ocorrencias[lancamento-1] += 1
    
for j in range(len(ocorrencias)):
    print("Número de ocorrencias do valor {0}: {1}".format(j+1, ocorrencias[j]))
    