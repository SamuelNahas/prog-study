n = 10

space = ''

for i in range(1, n+1):
    for j in range(1, i):
        space += " "
        print("{0}".format(space), end="")
    for k in range(i, 1, -1):
        print(k, end="")