n = int(input())
for i in range(1, n+1):
    somat = 0
    
    for j in range(1, i+1):
        if j == 1:
            print("{0}".format(j), end= ' ')
        else:
            print(" +{0}".format(j), end= ' ')
        somat += j

    print('= {0}'.format(somat))
    print()

