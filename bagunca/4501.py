# -*- coding: utf-8 -*-

"""
    Problema 4501 - Passa anel alterado
    Este é um jogo passa anel alterado que envolve J jogadores.
    Sempre haverá três jogadores principais, entre os J
    jogadores, das passagens de anel. O primeiro jogador
    principal passará o anel para o segundo jogador principal,
    após P passagens de anel, e então o segundo jogador
    principal passará o anel ao terceiro jogador principal,
    após S passagens de anel. Escreva um programa que leia a
    quantidade J de jogadores, P, e S, os J jogadores, e mostre
    quem é o primeiro jogador principal, o segundo jogador
    principal e o terceiro jogador principal. Os jogadores
    envolvidos na passagem do anel do primeiro jogador principal
    até o segundo jogador principal, e do segundo jogador
    principal até o terceiro jogador principal também precisam
    ser mostrados.

    Entrada
    Na primeira linha leia inteiros positivos J, P, e S,
    separados por espaço. É garantido que J >= 3 e P + S < J.
    Nas J linhas seguintes leia a identificação dos jogadores.
    Nunca haverá dois jogadores ou mais com a mesma
    identificação.

    Saída
    Mostre a identificação do primeiro jogador principal, na
    primeira linha. Na segunda linha mostre, em uma mesma linha,
    separados por espaço, a identificação dos jogadores, desde
    o primeiro jogador principal até o segundo jogador principal
    . Mostre a identificação do segundo jogador principal, na
    terceira linha. Na quarta linha mostre, em uma mesma linha,
    separados por espaço, a identificação dos jogadores, desde
    o segundo jogador principal até o terceiro jogador principal.
    Mostre a identificação do terceiro jogador principal, na
    quinta linha.

    Exemplo de Entrada:
    10 5 3
    A
    B
    C 
    D
    E 
    F
    G
    H 
    I 
    J

    Exemplo de Saída:
    Primeiro: A
    A B C D E F
    Segundo: F
    F G H I
    Terceiro: I
    
    Exemplo de entrada:
    6 3 2
    Ad
    Br
    Cl
    Ef
    Fe
    Ga
    
    Exemplo de saída:
    Primeiro: Ad
    Ad Br Cl Ef
    Segundo: Ef
    Ef Fe Ga
    Terceiro: Ga
"""

"""
    Ideia da solução:
    Primeiro lê se os três parâmetros de entrada com
    input().split() e transforma-os em int, gerando
    as variáveis j, p e s.
    Uma vez que precisa-se mostrar o que é necessário
    à medida que se lê cada identificação de jogador,
    faz-se um laço for de 0 a jogador-1 e utiliza-se
    o índice i para as decisões solicitadas no exercício.
    Utilizou-se esse intervalo de índices para facilitar
    o cálculo de qual jogador é o segundo e qual é terceiro.
    Dentro do laço for:
    O primeiro jogador é encontrado quando i == 0;
    O segundo jogador é encontrado quando i == p;
    O terceiro jogador é encontrado quando i == p+s;
    Os controles de não pular linha são feitos via
    parâmetro end = "" no print();
    Quando i == 0, mostra-se a identificação do jogador
    após "Primeiro: ", pula-se a linha, e mostra-se
    o jogador sem espaço após ele, e sem pular linha;
    Quando i < p, mostra-se espaço seguido de jogador,
    sem pular linha;
    Quando i == p, mostra-se espaço seguido de jogador,
    pulando linha, mostra-se a identificação do jogador
    após "Segundo: ", pula-se a linha, e mostra-se
    o jogador sem espaço após ele, e sem pular linha;
    Quando i < p+s, mostra-se espaço seguido de jogador,
    sem pular linha;
    Quando i == p+s, mostra-se espaço seguido de jogador,
    pulando linha, mostra-se a identificação do jogador
    após "Terceiro: ", pula-se a linha.
    Para i > p+s, a única ação será a leitura da identificação
    do jogador, sem saída relacionada.
"""

# j, p, s = Ler três inteiros
js, ps, ss = input().split()
j = int(js)
p = int(ps)
s = int(ss)

# para i de 0 a j-1
for i in range(j):
    # jogador = Ler identificação do jogador
    jogador = input()
    # se i == 0
    if i == 0:
        # Mostrar "Primeiro: " seguido de jogador
        print("Primeiro:", jogador)
        # Mostrar jogador sem pular linha
        print(jogador, end="")
    # senão se i < p
    elif i < p:
        # Mostrar " " seguido de jogador sem pular linha
        print("", jogador, end="")
    # senão se i == i + p
    elif i == p:
        # Mostrar " " seguido de jogador pulando linha
        print("", jogador)
        # Mostrar "Segundo: " seguido de jogador
        print("Segundo:", jogador)
        # Mostrar jogador sem pular linha
        print(jogador, end="")
    # senão se i < i + p + s
    elif i < p + s:
        # Mostrar " " seguido de jogador sem pular linha
        print("", jogador, end="")
    # senão se i == p + s
    elif i == p + s:
        # Mostrar " " seguido de jogador pulando linha
        print("", jogador)
        # Mostrar "Terceiro: " seguido de jogador
        print("Terceiro:", jogador)
        
        