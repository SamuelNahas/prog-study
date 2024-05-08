num = input()
d = input()

cont_ocorrencias = 0
for i in num:
    if i == d:
        cont_ocorrencias += 1
        
print(cont_ocorrencias)