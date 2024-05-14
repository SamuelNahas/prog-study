# -*- coding: utf-8 -*-

"""
    Problema 4497:
    Considere a sequência de potências de 3: 1, 3, 9, 27, ...
    E a sequência não potências de 3, que é sequência de valores inteiros
    positivos que não fazem parte da sequência de potências de 3:
    2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, ...
    Faça um programa que leia um inteiro i, que indica o i-ésimo termo da
    sequência não potências de 3. Mostre os valores da sequência não
    potências de 3 até o i-ésimo termo.

    Entrada
    Um inteiro positivo i.

    Saída
    Os valores da sequência não potências de 3 até o i-ésimo termo, separados
    por espaço, na mesma linha.  Após o i-ésimo termo deve-se pular linha.
    Não pode haver espaço após o i-ésimo termo nem antes do primeiro termo.

    Exemplo de Entrada:
    10

    Exemplo de Saída:
    2 4 5 6 7 8 10 11 12 13
"""

                   
"""
    Ideia da solução:
    A ideia é ir gerando a sequência de potências de 3 e a sequência não
    potências de 3 de forma sincronizada.
    
    O que complica a solução é a necessidade de atender aos requisitos de
    espaços na saída.
    Lemos primeiro o valor do i, já transformando para int.
    
    Definimos uma variável ate_i, inicialmente com 1, que irá indicar
    quantos termos da sequência não potências de 3 foram gerados.
    
    Primeiro se gera uma potência de 3 e então os números não potência de 3
    até uma unidade antes desse número potência de 3,
    então gera-se uma nova potência de 3 e os novos números não potência de 3
    até uma unidade antes desse outro número potência de 3, e assim
    sucessivamente, até que se chegue ao i-ésimo número não potência de 3.
    À medida que cada número não potência de 3 é gerado, ele é mostrado.
    
    Não se utilizou os valores iniciais de 1 e
    3, respectivamente porque sempre iremos mostrar primeiro
    o 2, que é o primeiro termo da sequência não potências de 3.
       
    Pensou-se em dois casos:
    1) Quando i == 1: neste caso basta mostrar 2 e pular linha
    2) Quando i > 1: neste caso precisamos primeiro mostrar 2 sem pular linha.
    Definimos npot3 com 4 e ate_i com 2. 4 é o segundo número não potência de 3.
    Definimos pot3 para 9.
    E então fazemos um laço while True para gerar a sequência solicitada.
    Dentro desse laço while ate_i <= i:
    2.1) Fazemos um novo while npot3 < pot3-1 and ate_i < i, que mostra
    um espaço seguido de um número não potência de 3 até pot3-2, e gera números
    não potência de 3 até pot3-1.
    2.2) Logo após o laço while, se ate_i == i, mostra-se um espaço seguido
    do último número não potência de 3 gerado, pula-se linha
    e sai do laço while ate_i <= i com break.
    Caso contrário, npot3 == pot3-1, e mostra-se um espaço seguido de
    pot3-1 um número não potência de 3, atualiza-se o novo número não
    potência de 3 para ser um a mais do que pot3 e incrementa em uma unidade
    ate_1. Por fim, gera-se um novo número potência de 3 em pot3.
"""

# i = Ler um inteiro
i = int(input())

# se i == 1:
if i == 1:
    # Mostrar termo
    print(2)
#senão
else:
    # Mostrar termo
    print(2, end="")

    # npot3 = 4
    npot3 = 4

    # ate_i = 2
    ate_i = 2
    
    # pot3 = 9
    pot3 = 9
    
    # Laço enquanto para geração dos números
    # enquanto ate_i <= i
    while ate_i <= i:    
        # enquanto termo_k <= termo_i e k_esimo < K
        while npot3 < pot3-1 and ate_i < i:
            # Mostrar " " seguido de npot3
            print("", npot3, end="")          
            # Gera novo número não potência de 3
            npot3 += 1
            # Incrementa o contador de novo termo de Fibonot
            ate_i += 1

        # se ate_i == i
        if ate_i == i:
            # Mostrar " " seguido de npot3
            print("", npot3)              
            # Sair do laço
            break
        # senão se se npot3 == pot3-1
        else: # if npot3 == pot3-1:
            # Mostrar " " seguido de npot3
            print("", npot3, end="")
            
            # Atualizar o novo número não potência de 3 para ser um
            # a mais do que pot3.
            npot3 = pot3 + 1
            # Incrementa o contador de número não potência de 3
            ate_i += 1
            
            # Gerar próxima potência de 3
            pot3 *= 3
         
