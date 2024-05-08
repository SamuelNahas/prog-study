x = int(input())
i = 1
somatorio = 0
sup = 2

while i <= 30:
    somatorio += (sup*(x**sup))/2*sup

    sup += 1
    i += 1

print("{0:.4f}".format(x+somatorio))