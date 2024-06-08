def busca_binaria(vetor, elemento):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == elemento:
            return meio
        elif vetor[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1

    return "O elemento não está presente na lista"

vetor = []
for i in range(1, 3000):
    vetor.append(i)
    
elemento = int(input())

print(busca_binaria(vetor, elemento))
# 1 (índice do elemento)