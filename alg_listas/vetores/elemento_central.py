lista = list(map(int, input().split()))
tam = len(lista)
flag = 0

if tam % 2 != 0:
    elemento_1 = (tam//2)
else:
    elemento_1 = (tam//2)-1
    elemento_2 = (tam//2)
    flag = 1
    
if flag:
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()
    print("Elementos centrais da lista: {0} e {1}".format(lista[elemento_1], lista[elemento_2]))
else:
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()
    print("Elemento central da lista:",lista[elemento_1])        