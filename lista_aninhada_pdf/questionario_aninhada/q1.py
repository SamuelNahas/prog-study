m = int(input())
n = int(input())

for i in range(m, n+1):
    print("Lista de divisores de {0}".format(i))
    for j in range(1, i+1):
        if i % j == 0:
            if j == i:
                print(j)
            else:
                print(j, end=", ")
    print()

