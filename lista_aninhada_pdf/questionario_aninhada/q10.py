n = int(input())

for i in range(n):
    fatorial = int(input())
    soma_fatorial = 1
    for j in range(1, fatorial+1):
        soma_fatorial *= j
    print("{0}! = {1}".format(fatorial, soma_fatorial))