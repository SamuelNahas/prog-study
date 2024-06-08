# Leia as informações de idades e alturas de 30 pessoas. 
# Determine quantas pessoas com mais de 13 anos possuem altura inferior a média das alturas.

lista_idade = []
lista_altura = []

for i in range(5):
    i, a = map(float, input().split())
    lista_idade.append(i)
    lista_altura.append(a)

media_altura = 0
for k in range(5):
    media_altura += lista_altura[k]

media_altura = media_altura/5

cont_pessoas = 0

for j in range(5):
    if lista_idade[j] > 13 and lista_altura[j] < media_altura:
        cont_pessoas += 1         

print(media_altura)
print(cont_pessoas)