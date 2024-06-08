lista_nome = list(input().split())
lista_idade = list(map(int, input().split()))
novo_nome = input()
nova_idade = int((input()))

flag = 0
tam = len(lista_idade)
for i in range(tam):
    if lista_idade[i] <= nova_idade:
        if lista_idade[i] == nova_idade:
            indice_insercao = i + 1
            flag = 1
        else:
            indice_insercao = i 
            flag = 1
        break

if flag:
    lista_idade.append(-1)
    lista_nome.append(-1)
    for j in range(tam, indice_insercao, -1):
        lista_idade[j] = lista_idade[j-1]
        lista_nome[j] = lista_nome[j-1]
    lista_idade[indice_insercao] = nova_idade
    lista_nome[indice_insercao] = novo_nome
    print("Fila atualizada")
    print(lista_nome)
    print(lista_idade)
else:
    lista_idade.append(nova_idade)
    lista_nome.append(novo_nome)
    print("Fila atualizada")
    print(lista_nome)
    print(lista_idade)