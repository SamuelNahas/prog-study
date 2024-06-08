def seq(x, j):
    lista_resultado = []
    somatorio = 0
    it = 1
    for i in range(x, j+1):
        termo = (i**it)/it
        lista_resultado.append(termo)
        somatorio += termo
        it += 1
    
    return lista_resultado, somatorio

base = int(input())
sup = int(input())

lista, somatorio = seq(base, sup)

for i in range(len(lista)):
    print(lista[i], end=' ')
print()
print()
print("O valor do somatório é:", somatorio)