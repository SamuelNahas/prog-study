number = int(input())

for i in range(1, number+1):
    soma = 0
    for j in range(1, i+1):
        if j != i:
            print(j, end=" + ")
        else:
            print(j, end=" ")
            
        soma += j
    print("=", soma)