# -*- coding: utf-8 -*-

"""
    Problema 4499 - Operações aritméticas
    Faça um programa que implemente uma calculadora especial que
    pode utilizar as operações de soma, subtração, multiplicação,
    divisão e potenciação, via operadores binários +, -, *, /, **. O operador unário - também pode ser utilizado.
    A ordem de precedência é 1) - unário; 2) **; 3) * e /; e
    4) + e -.

    Contudo, a entrada pode ser uma operação com um único
    operador binário por linha no formato operando
    operadorbinário operando, ou "total". Os operandos e
    operadores binários são separados por espaços.
    O operador unário - deve ser utilizado colado ao número.
    Pode haver várias operações e zero ou mais linhas com "total".

    Se a entrada for "total", mostra-se o valor acumulado e
    zera-se o valor acumulado. Se for uma operação aritmética,
    realiza-se a operação, e o resultado deve ser acumulado pela
    soma. 

    Se a última entrada não for "total", deve-se mostrar
    "Faltou pedir para mostrar " seguido do valor acumulado.
    Caso contrário, deve-se mostrar "Os acumulados foram mostrados".

    Entrada
    Há um número indefinido de linhas de entrada.
    Uma linha de entrada pode ter somente dois operandos e um 
    operador binário, separados por espaços, ou "total". A entrada
    termina com EOF.

    Saída
    De acordo com o enunciado do problema, com a condição devida,
    deve ser mostrado o valor acumulado, "Faltou pedir para mostrar "
    seguido do valor acumulado, ou "Os acumulados foram mostrados".
    Os valores numéricos precisam ser mostrados em ponto flutuante
    com duas casas decimais.
    
    Exemplo de entrada:
    total
    3 ** 4
    -1.5 + 2.7
    total
    
    Exemplo de saída:
    0.00
    82.20
    Os acumulados foram mostrados
    
    Exemplo de entrada:
    4 / 2
    3 - 100
    7 * 8
    total
    100 + 50
    
    Exemplo de saída:
    -39.00
    Faltou pedir para mostrar 150.00
"""

"""
    Ideia da solução:
    Uma vez que temos que mostrar os valores acumulados
    que são calculados, utiliza-se uma variável contadora
    acumulado, inicialmente com 0.0.
    Precisamos saber se a última linha de entrada
    foi "total" ou não, e utiliza-se a variável lógica
    total_eh_ultimo, inicialmente com False.
    A entrada termina com EOF, então defini-se um laço
    while True que terminará com a ocorrência da
    exceção EOFError.
    Dentro do laço while:
    Controlamos a leitura de uma linha de entrada
    utilizando um bloco try/except EOFError. Se
    conseguir ler, a linha lida é armazenada na
    variável ent. Caso contrário, utiliza-se break
    para sair do laço while.
    Se a ent == "total" utiliza-se formatação de saída
    com .2f para mostrar o valor de acumulado com
    duas casas decimais, zera-se o valor de acumulado,
    e registra-se que a entrada foi "total" colocando
    total_eh_ultimo em True.
    Caso contrário, registra-se que a entrada não foi
    "total" colocando total_eh_ultimo em False, sabe-se que
    ent contém uma operação aritmética
    e utiliza-se ent.split() para obter os operandos
    e o operador, tomando o cuidado de transformar
    os operandos em float. Pela comparação do operador
    realiza-se a operação aritmética solicitada e o
    resultado é armazenado em acumulado.
    Se total_eh_ultimo é True, mostra-se
    "Os acumulados foram mostrados". Caso contrário,
    mostra-se "Faltou pedir para mostrar " seguido
    do valor de acumulado com duas casas decimais,
    com formatação de saída utilizando .2f.
"""

# acumulado = 0.0
acumulado = 0.0

# total_eh_ultimo = falso
total_eh_ultimo = False

# Enquanto verdadeiro
while True:
    # Tentar
    try:
        # ent = Ler entrada
        ent = input()
    # Se EOF
    except EOFError:
        # Sair do enquanto
        break
    # se ent == "total"
    if ent == "total":
        # Mostrar acumulado com duas casas decimais
        print("{0:.2f}".format(acumulado))
        # acumulado = 0.0
        acumulado = 0.0
        # total_eh_ultimo = verdadeiro
        total_eh_ultimo = True
    # senão
    else:
        # total_eh_ultimo = falso
        total_eh_ultimo = False
        # op1, opera, op2 = Separar a entrada
        op1s, opera, op2s = ent.split()
        op1 = float(op1s)
        op2 = float(op2s)
        # se opera == "+"
        if opera == "+":
            # acumulado += op1 + op2
            acumulado += op1 + op2
        #senão se opera == "-"
        elif opera == "-":
            # acumulado += op1 - op2
            acumulado += op1 - op2
        #senão se opera == "*"
        elif opera == "*":
            # acumulado += op1 * op2
            acumulado += op1 * op2
        #senão se opera == "/"
        elif opera == "/":
            # acumulado += op1 / op2
            acumulado += op1 / op2
        #senão se opera == "**"
        else:
            # acumulado += op1 ** op2
            acumulado += op1 ** op2
# se total_eh_ultimo
if total_eh_ultimo:
    # Mostrar "Os acumulados foram mostrados"
    print("Os acumulados foram mostrados")
# senão
else:
    # Mostrar "Faltou pedir para mostrar " acumulado
    print("Faltou pedir para mostrar {0:.2f}".format(acumulado))
    