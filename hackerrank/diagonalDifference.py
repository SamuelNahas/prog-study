def somar_diagonal_principal(matriz):
  soma = 0
  for i in range(len(matriz)):
    soma += matriz[i][i]
  return soma

def somar_diagonal_secundaria(matriz):
  soma = 0
  j = len(matriz) - 1
  for i in range(len(matriz)):
    print(j)
    soma += matriz[i][j]
    j -= 1
    if j == -1:
        break
  return soma

matriz = [[1, 2, 5],
          [4, 5, 6],
          [7, 8, 9]]

soma_diagonal_principal = somar_diagonal_principal(matriz)
soma_diagonal_secundaria = somar_diagonal_secundaria(matriz)

print(f"Soma da diagonal principal: {soma_diagonal_principal, soma_diagonal_secundaria}")
