n = int(input())
cont = 0

for i in range(500, n+1):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")
        cont += 1
        if cont % 10 == 0:
            print()
        
    