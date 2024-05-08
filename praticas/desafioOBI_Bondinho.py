alunos, monitores = map(int, input().split())
somaPessoas = alunos + monitores

divisaoBondeInteira = somaPessoas // 50
divisaoBonde = somaPessoas / 50

if somaPessoas <= 50:
    print("Todos subirão juntos!")
elif divisaoBonde % 1 != 0:
    print("Você precisará de {0} viagens para levar todos!".format(divisaoBondeInteira+1))
else:
    print("Você precisará de {0} viagens para levar todos!".format(divisaoBondeInteira))
