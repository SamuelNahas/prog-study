tam_seq = int(input())
anterior = int(input())
flag = 1

for i in range(tam_seq-1):
    valor = int(input())
    
    if valor <= anterior:
        flag = 0
    
    anterior = valor
    
if flag:
    print("crescente")
else:
    print("sem ordem")
    
    