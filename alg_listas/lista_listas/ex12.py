n = int(input())
lista_termos = []
lista_cima = []
lista_baixo = []

for i in range(n, 0, -1):
    lista_termos.append(i)

for j in range(24):
    lista_cima.append(lista_termos[j])
for k in range(49, 24, -1):
    lista_baixo.append(lista_termos[k])

lista_result = []
for l in range(len(lista_cima)):
    soma = 0
    soma = lista_cima[i] + lista_baixo[i]
    lista_result.append(soma)

print(lista_result)

