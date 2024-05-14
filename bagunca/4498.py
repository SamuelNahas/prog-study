# -*- coding: utf-8 -*-

"""
    Problema 4498 - Sequência Lógica IS
    Escreva um programa que leia um valor inteiro N e mostre N * 3
    linhas de saída, seguindo a lógica do exemplo abaixo. 

    Entrada
    O arquivo de entrada contém um número inteiro positivo N.

    Saída
    Imprima a saída conforme a lógica do exemplo fornecido.
    Há espaço em branco entre os valores e não há espaço em branco
    antes do primeiro e depois do último valores de cada linha.

    Exemplo de Entrada
    4

    Exemplo de Saída
    2 1 4
    2 0 5
    2 -1 6 
    4 3 6
    4 2 7
    4 1 8
    6 5 8
    6 4 9
    6 3 10
    8 7 10
    8 6 11
    8 5 12
"""

"""
    Ideia da solução:
    Primeiro lemos o número inteiro em n.
    Depois fazemos um laço for de 1 a n, com iterador i.
    Dentro do laço for, utilizamos a lógica do exemplo
    dado para mostrar os valores:
    Em cada linha temos valores derivados de 2*i.
    Então fazemos fator = 2*i.
    Na primeira linha de cada repetição temos o padrão
    fator fator-1 fator+2, e mostramos de acordo.
    Na segunda linha de cada repetição temos o padrão
    fator fator-2 fator+3, e mostramos de acordo.
    Na terceira linha de cada repetição temos o padrão
    fator fator-3 fator+4, e mostramos de acordo.
"""

# n = Ler número inteiro
n = int(input())

# para i de 1 até n
for i in range(1, n+1):
    fator = 2*i
    # Mostrar fator fator-1 fator+2
    print(fator, fator-1, fator+2)
    # Mostrar fator fator-2 fator+3
    print(fator, fator-2, fator+3)
    # Mostrar fator fator-3 fator+4
    print(fator, fator-3, fator+4)
    