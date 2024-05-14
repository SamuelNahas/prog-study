def binToDec(number):
    valor_inicial = number
    soma_binario = 0
    potencia_2 = 1
    
    while number != 0:
        digito_atual = number%10
        soma_binario += potencia_2 * digito_atual
        potencia_2 *= 2
        number//=10
    
    print(valor_inicial, "=", soma_binario)

binToDec(1001010)