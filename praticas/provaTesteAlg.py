
#! QUESTAO 1
# matricula, turma, mediaFinal = input().split()

# matricula = int(matricula)
# mediaFinal = float(mediaFinal)

# print("O estudante de matrícula {0}, turma {1}, obteve média = {2:.2f}.".format(matricula, turma, mediaFinal))

#! QUESTAO 2
# valor, juros = input().split()
# valor = int(valor)
# juros = float(juros)

# valorComJuros = valor + valor * (juros/100)
# rendimento = valor * (juros/100)

# print("{0:.2f} {1:.2f}".format(rendimento, valorComJuros))

# ! QUESTAO 3
# nota1, nota2, nota3 = map(float, input().split())
# cargaDisc = int(input())
# cargaAluno = int(input())

# mediaAluno = (nota1 + nota2 + nota3)/3
# frequenciaPorcento = (cargaAluno/cargaDisc)*100

# if mediaAluno < 6 or frequenciaPorcento < 75:
#     print("Reprovado")
# else: 
#     print("Aprovado")

#! QUESTAO 4
# alunos = int(input())
# monitores = int(input())
# somaPessoas = alunos + monitores

# divisaoBondeInteira = somaPessoas // 50
# divisaoBonde = somaPessoas / 50

# if somaPessoas <= 50:
#     print("Todos podem subir juntos!")
# elif divisaoBonde % 1 != 0:
#     print("São necessárias no mínimo {0} viagens para levar todos vocês!".format(divisaoBondeInteira+1))
# else:
#     print("São necessárias no mínimo {0} viagens para levar todos vocês!".format(divisaoBondeInteira))
