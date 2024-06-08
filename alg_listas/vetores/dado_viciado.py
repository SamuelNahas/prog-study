lista = list(map(int, input().split()))
registro_dados = [i for i in range(6)]


for i in range(len(lista)):
    element = lista[i]
    registro_dados[element-1] += 1

print("Lançamentos:", lista)
for j in range(len(registro_dados)):
    print("Número de ocorrências da face {0} = {1}".format(j+1, registro_dados[j]))
