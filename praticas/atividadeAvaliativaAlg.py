# numeroReal = float(input())

# if numeroReal >= 0:
#     print("|{0:.2f}| = {1:.2f}".format(numeroReal, numeroReal))
# else: 
#     print("|{0:.2f}| = {1:.2f}".format(numeroReal, -numeroReal))

# salario = float(input())

# if salario >= 0 and salario <= 400:
#     print("Novo salario: R$ {0:.2f}".format(salario * 1.2))
#     print("Reajuste ganho: R$ {0:.2f}".format(salario * 0.2))
#     print("Em percentual: 20%")
# elif salario > 400 and salario <= 800:
#     print("Novo salario: R$ {0:.2f}".format(salario * 1.17))
#     print("Reajuste ganho: R$ {0:.2f}".format(salario * 0.17))
#     print("Em percentual: 17%")
# elif salario > 800 and salario <= 1200:
#     print("Novo salario: R$ {0:.2f}".format(salario * 1.13))
#     print("Reajuste ganho: R$ {0:.2f}".format(salario * 0.13))
#     print("Em percentual: 13%")
# elif salario > 1200 and salario <= 2000:
#     print("Novo salario: R$ {0:.2f}".format(salario * 1.08))
#     print("Reajuste ganho: R$ {0:.2f}".format(salario * 0.08))
#     print("Em percentual: 8%")
# else:
#     print("Novo salario: R$ {0:.2f}".format(salario * 1.05))
#     print("Reajuste ganho: R$ {0:.2f}".format(salario * 0.05))
#     print("Em percentual: 5%")

# a, b, c = map(int, input().split())

# def delta(a, b, c):
#     return ((b*b)-4*a*c)

# def bhaskara(a, b, c):
#     if delta(a, b, c) < 0 or a == 0:
#         print("Impossível calcular")
#     elif delta(a, b, c) == 0:
#         raizReal = -b/2*a
#         print("A equação possui apenas uma raiz real. Raiz = {0}".format(raizReal))
#     else:
#         raiz1 = (-b - delta(a, b, c)**(1/2))/(2*a)
#         raiz2 = (-b + delta(a, b, c)**(1/2))/(2*a)
#         print("Raiz 1 =", raiz1)
#         print("Raiz 2 =", raiz2)

# bhaskara(a, b, c)

# bandeira, gastoKWH = input().split()
# gastoKWH = int(gastoKWH)

# valorBaseKWH = 0.809

# if bandeira == "verde" and gastoKWH > 100:
#     print("Custo da Energia R${0:.2f}".format(gastoKWH * valorBaseKWH))
# elif gastoKWH <= 100 and bandeira == "verde":
#     print("Custo da Energia R${0:.2f}".format(100 * valorBaseKWH))
# elif gastoKWH <= 100 and bandeira == "amarela":
#     print("Custo da Energia R${0:.2f}".format(100 * (valorBaseKWH+0.01)))
# elif gastoKWH <= 100 and bandeira == "preta":
#     print("Custo da Energia R${0:.2f}".format(100 * (valorBaseKWH+0.05)))
# elif gastoKWH <= 100 and bandeira == "vermelha":
#     print("Custo da Energia R${0:.2f}".format(100 * (valorBaseKWH+0.03)))
# elif bandeira == "amarela":
#     print("Custo da Energia R${0:.2f}".format(gastoKWH * (valorBaseKWH+0.01)))
# elif bandeira == "preta":
#     print("Custo da Energia R${0:.2f}".format(gastoKWH * (valorBaseKWH+0.05)))
# elif bandeira == "vermelha":
#     print("Custo da Energia R${0:.2f}".format(gastoKWH * (valorBaseKWH+0.03)))
    
# mes = int(input())
# if mes == 2:
#     print("O mês possui 28 dias")
# elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#     print("O mês possui 31 dias")
# else:
#     print("O mês possui 30 dias")

# num1 = int(input())
# num2 = int(input())

# if num2 % num1 != 0:
#     print("{0} não é divisor de {1}".format(num1, num2))
# else:
#     print("{0} é divisor de {1}".format(num1, num2))

# empresa1, materiais1, maoDeObra1 = input().split()
# empresa2, materiais2, maoDeObra2 = input().split()
# materiais1 = float(materiais1)
# materiais2 = float(materiais2)
# maoDeObra1 = float(maoDeObra1)
# maoDeObra2 = float(maoDeObra2)

# if (materiais1 + maoDeObra1) == (materiais2 + maoDeObra2):
#     print("As empresas apresentaram o mesmo valor no orçamento.")
# elif (materiais1 + maoDeObra1) > (materiais2 + maoDeObra2):
#     print("Melhor orçamento = {0}.".format(empresa2))
# elif (materiais1 + maoDeObra1) < (materiais2 + maoDeObra2):
#     print("Melhor orçamento = {0}.".format(empresa1))

# def isEven(valor):
#     return not bool(valor&1)

# numero = int(input())

# if numero == 0:
#     print("O número informado é 0.")
# elif isEven(numero) and numero < 0:
#     print("Par e negativo")
# elif isEven(numero) and numero > 0:
#     print("Par e positivo")
# elif not isEven(numero) and numero < 0:
#     print("Impar e negativo")
# elif not isEven(numero) and numero > 0:
#     print("Impar e positivo")

# x = int(input())
# y = int(input())

# if x == 0 and y == 0:
#     print("Origem")
    
    
# elif x > 0:
#     if y > 0:
#         print("Quadrante 1")
#     elif y < 0:
#         print("Quadrante 4")
#     elif y == 0:
#         print("O ponto está no eixo x (positivo)")
# else:
#     if y > 0:
#         print("Quadrante 2")
#     elif y < 0:
#         print("Quadrante 3")
#     elif y == 0:
#         print("O ponto está no eixo x (negativo)")

# diametro = int(input())*2
# altura, largura, profundidade = input().split()

# if(diametro <= int(altura) and diametro <= int(largura) and diametro <= int(profundidade)):
#     print("S")
# else:
#     print("N")

# hora2, minuto2, segundo2 = map(int, input().split(":"))
# hora1, minuto1, segundo1 = map(int, input().split(":"))

# diferencaSegundo = segundo1 - segundo2
# diferencaMinuto = minuto1 - minuto2
# diferencaHora = hora1 - hora2


# if hora2 > hora1:
#     if diferencaSegundo < 0:
#         if(diferencaMinuto > 0):
#             print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora + 24, diferencaMinuto - 1, 60 - (diferencaSegundo * -1)))
#         else:
#             print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora +23, 59 - (diferencaMinuto * -1), 60 - (diferencaSegundo)* -1))
#     else:
#         if(diferencaMinuto < 0):
#             print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora+24, 60 - (diferencaMinuto * -1), diferencaSegundo))
#         else:
#             print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora+24, diferencaMinuto, diferencaSegundo))                

# elif diferencaSegundo < 0:
#     if(diferencaMinuto > 0):
#         print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora, diferencaMinuto - 1, 60 - (diferencaSegundo * -1)))
#     else:
#         print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora - 1, 59 - (diferencaMinuto * -1), 60 - (diferencaSegundo)* -1))

# else:
#     if(diferencaMinuto < 0):
#         print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora-1, 60 - (diferencaMinuto * -1), diferencaSegundo))
#     else:
#         print("Tempo de jogo: {0}:{1}:{2}".format(diferencaHora, diferencaMinuto, diferencaSegundo))

# Entrada de dados
valorCompra = int(input())
valorPago = int(input())
valor = valorPago - valorCompra
# Processamento
notas50 = valor // 50
resto50 = valor % 50

notas10 = resto50//10
resto10 = resto50%10

notas5 = resto10//5
resto5 = resto10%5

notas1 = resto5//1

# Saída
if notas50 != 0:
    if notas50 == 1:
        print("1 nota de 50".format(notas50))
    else:
        print("{0} notas de 50".format(notas50))
if notas10 != 0:
    if notas10 == 1:
        print("1 nota de 10".format(notas10))
    else:
        print("{0} notas de 10".format(notas10))
if notas5 != 0:
    if notas5 == 1:
        print("{0} nota de 5".format(notas5))
    else:    
        print("{0} notas de 5".format(notas5))
if notas1 != 0:
    if notas1 == 1:
        print("{0} nota de 1".format(notas1))
    else:
        print("{0} notas de 1".format(notas1))