num = int(input())

soma_divisores = 0

for i in range(1, num, 1):
    if num%i==0: 
        soma_divisores += i

if soma_divisores < num:
    print("{0} deficiente".format(num))
elif soma_divisores == num: 
    print("{0} perfeito".format(num))
else: 
    print("{0} abundante".format(num))