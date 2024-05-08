# x = float(input())
# y = float(input())
# e = float(input())

# #Foram realizadas it iterações para se determinar o valor aproximado para a raiz quadrada de x.2f que é valor_raiz.5f

# y_ant = 0
# y_at = 0
# it = 0

# while True:
#     it += 1
    
#     div_xy = x/y
#     raiz_aprox = (y + (x/y))/2
    
#     if (y_ant - y_at) == 0:
#         y_at = y
#         y_ant = raiz_aprox
#         continue
#     else:
#         dif = y_ant - y_at
        
#         if dif <= e:
#             print("Foram realizadas {0:.2f} iterações para se determinar o valor aproximado para a raiz quadrada de {1:.2f} que é {2}".format(it, x, raiz_aprox))
#             break
#         else:
#             continue


def raiz_quadrada(x, y, e):
  iteracoes = 0
  while True:
    iteracoes += 1
    y_anterior = y
    y_atual = ((y + (x / y)) / 2)
    
    if y_anterior > y_atual:
      dif = y_anterior - y_atual
    else:
      dif = y_atual - y_anterior 
  
    if dif <= e:
        return y_atual, iteracoes
    else:
        y = y_atual
      



# Exemplo de uso
x = float(input())
y = float(input())
e = float(input())

raiz_aproximada, iteracoes = raiz_quadrada(x, y, e)

print("Foram realizadas {0} iterações para se determinar o valor aproximado para a raiz quadrada de {1:.2f} que é {2:.5f}".format(iteracoes, x, raiz_aproximada))
