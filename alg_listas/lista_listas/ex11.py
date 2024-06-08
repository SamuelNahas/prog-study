x = int(input())

soma = x
sup = 2
lista_termos = []

for i in range(1, 100):
    termo = (sup*x**sup)/sup**sup
    soma += termo
    lista_termos.append(termo)
    sup += 1

media = soma/100

termos_abaixo_media = 0
for i in range(len(lista_termos)):
    if lista_termos[i] < media:
        termos_abaixo_media += 1
        
print(media, termos_abaixo_media)