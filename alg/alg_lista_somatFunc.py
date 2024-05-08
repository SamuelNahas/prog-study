x = int(input())


somat = 0
aux = 2
cont = 2
while cont < 31:
    somat += (0.5*(x**aux))
    aux += 1
    cont += 1

print("{0:.4f}".format((somat+x)/x))

