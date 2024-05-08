i = 1
numb = 3

primos = []
verificadores = [1]

cont = 1
while True:
    if cont == 30:
        break
    
    if numb % i == 0:
        i += 1
        continue
    else:
        print(numb)
        cont += 1
        verificadores.append(i)


print(verificadores)