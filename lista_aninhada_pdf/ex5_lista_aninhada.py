n = 10

space = ''

for i in range(1, n+1):
    for j in range(1, 10):
        space += "  "
        print("{0}{1}".format(space, j))
    