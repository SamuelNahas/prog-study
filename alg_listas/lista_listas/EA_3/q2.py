def fatorial(numb):
    somat = 1
    for i in range(1, numb+1):
        somat *= i
    return somat

x, epsilon = map(float, input().split())

i = 1
soma = 0
while True:
    termo = (x**i)/fatorial(i) 
    i += 1
    if termo < epsilon:
        break
    
    soma += termo
      
result = 1 + soma
print("cos({0:.7f}) = {1:.7f}".format(x, result))