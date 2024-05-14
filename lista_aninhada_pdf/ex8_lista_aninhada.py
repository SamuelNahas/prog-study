interval = range(101, 277)
divis = []

for i in interval:
    for j in range(i):
        if j % i == 0:
            divis.append(j)

print(divis)