salario = float(input())

def imposto_de_renda(salario):
    if salario <= 2000:
        print("Isento")
    elif salario > 2000 and salario <= 3000:
        print('R$ ') . salario * 0.08
    elif salario > 3000 and salario <= 4500:
        print('R$ ') . salario * 0.18
    elif salario > 4500:
        print('R$ ') . salario * 0.28
        
imposto_de_renda(salario)