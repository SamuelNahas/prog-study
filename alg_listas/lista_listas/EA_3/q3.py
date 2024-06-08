def fatorial(numb):
    somat = 1
    for i in range(1, numb+1):
        somat *= i
    return somat

x = float(input())
num = int(input())

aux = 2
soma_termos = 0
for i in range(2, num+1):
    termo = (x**aux)/fatorial(aux) 
    aux += 2
    
    if i % 2 == 0:
        soma_termos += termo
    else:
        soma_termos -= termo
        
result = 1 - soma_termos
print("cos({0:.6f}) = {1:.6f}".format(x, result))