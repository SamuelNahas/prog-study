matriz = [list(map(int, input().split())) for i in range(int(input()))]
linhas = len(matriz)
colunas = len(matriz[0])
rota = list(map(int, input().split()))

custo_itinerario = 0
for i in range(len(rota)-1):
    origem = rota[i]-1
    destino = rota[i+1]-1
    
    custo_itinerario += matriz[origem][destino]

print("Custo do itinerário informado = {0:.1f}".format(float(custo_itinerario)))


