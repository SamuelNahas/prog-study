

result = ""

for i in range(101, 278):
    for j in range(1, (i+1)):
        if j % i == 0:
            result += "\n{0}".format(i)            

print(result)