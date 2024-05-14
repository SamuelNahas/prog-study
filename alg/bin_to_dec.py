def binToDec(number):
    valor_inicial = number
    saida = 0
    potencia_2 = 1
    
    while number != 0:
        digito_atual = number%10
        saida += potencia_2 * digito_atual
        potencia_2 *= 2
        number//=10
    
    print(valor_inicial, "=", saida)

binToDec(1001010)