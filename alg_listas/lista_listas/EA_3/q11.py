x = int(input())
y = int(input())
somatorio = 0
for i in range(1, y+1):
    termo = (i * (x**i))/i**2
    print("{0:.3f}".format(termo), end=" ")
    somatorio += termo
print()
print()
print("O valor do somatório é: {0:.4f}".format(somatorio))