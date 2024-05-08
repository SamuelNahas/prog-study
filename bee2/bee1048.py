salario = float(input())

def reajuste_salarial(salario):
    if salario <= 400:
        novoSalario = salario * 1.15
        ganho = novoSalario - salario
        percentual = 15
    elif salario > 400 and salario <= 800:
        novoSalario = salario * 1.12
        ganho = novoSalario - salario
        percentual = 12
    elif salario > 800 and salario <= 1200:
        novoSalario = salario * 1.1
        ganho = novoSalario - salario
        percentual = 10
    elif salario > 1200 and salario <= 2000:
        novoSalario = salario * 1.07
        ganho = novoSalario - salario
        percentual = 7
    else:
        novoSalario = salario * 1.04
        ganho = novoSalario - salario
        percentual = 4
    print(f"Novo salario: {novoSalario:.2f}")
    print(f"Reajuste ganho: {ganho:.2f}")
    print(f"Em percentual: {percentual} %")
    
reajuste_salarial(salario)