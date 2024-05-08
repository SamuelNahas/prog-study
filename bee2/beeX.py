standard_input = [2, 2, "CBA", "DDD", 6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]


def retornaValorAlfabeto(letra):
  letra = letra.upper()
  # Retorna o valor da letra
  return ord(letra) - ord('A')


qtdeEntradas = int(input())
saidas = []


for a in range(qtdeEntradas):
    qtdeString = int(input())
   
    for i in range(qtdeString):
        stringHash = input()
        somatorio = 0


        for j in range(len(stringHash)):
            somatorio = somatorio + retornaValorAlfabeto(stringHash[j]) + i + j + a


    saidas.append(somatorio)
    
   


   
    saidaFinal = []
    saidaFinalSuporte = 0
    for k in range(len(saidas)):
        saidaFinalSuporte = saidaFinalSuporte + saidas[k]
        saidaFinal.append(saidaFinalSuporte)
        saidaFinalSuporte = 0



print(saidaFinal)
