n = int(input())

cont = 0
somatorio = 0

lista_notas = []
for i in range(n):
    nota = float(input())
    
    lista_notas.append(nota)
    somatorio += nota
    cont += 1    

media = somatorio/cont
print("A turma teve média de {0:.2f} nesta avaliação".format(media))

contador_menores = 0
contador_maiores = 0
for j in range(len(lista_notas)):
    if lista_notas[i] >= media:
        contador_maiores += 1
    else:
        contador_menores += 1

print("{0} alunos tiveram nota maior ou igual a média".format(contador_maiores))
print("{0} alunos tiveram nota menor ou igual a média".format(contador_menores)) 
