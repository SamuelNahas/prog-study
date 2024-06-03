n = int(input())

resultado = "Seguem os valores dos fatorais de cada um dos inteiros informados:"
for i in range(n):
    fatorial = int(input())
    soma_fatorial = 1
    for j in range(1, fatorial+1):
        soma_fatorial *= j
    resultado += "\n{0}! = {1}".format(fatorial, soma_fatorial)
    
print(resultado)