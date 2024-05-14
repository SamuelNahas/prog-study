lim = int(input())

for i in range(1, lim+1):
    for j in range(lim-i):
        print(" ", end="")
    for k in range(i):
        print("+", end=" ")
    print()
