# Leia um conjunto de n valores inteiros, para 1 ≤ n ≤ 30, e imprima o elemento central. Para n par, deve-se considerar a existência de 2 elementos centrais. Exemplos: a sequência 5, 223, 76, 19, 0, 43, 5 o elemento central é 19, já a sequência 44, 6, 89, 6, 2, 5, 77, 43, 27, 94 possui dois elementos centrais: 2 e 5

n = int(input())

lista_valores = []

for i in range(n):
    lista_valores.append(int(input()))
    
if n % 2 != 0:
    print(lista_valores[n//2])
else:
    valor_1 = (n//2)-1
    valor_2 = n//2
    
    print("{0} e {1}".format(lista_valores[valor_1], lista_valores[valor_2]))