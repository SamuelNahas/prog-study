cont = 1

for i in range(1, 400, 2):
    print(i, end=' ')
    if cont % 10 == 0:
        print('')
    cont += 1