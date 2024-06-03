n = int(input())

primos = 0
cand = 2
cont = 0

while primos < n:
    flag = 1
    for j in range(2, cand):
        if cand % j == 0:
            flag = 0
            break
    if flag:
        print(cand, end=' ')
        cont += 1
        if cont % 10 == 0:
            print()
        primos += 1
    cand += 1