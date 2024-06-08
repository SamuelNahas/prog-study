# Leia duas sequências numéricas de tamanho 10 cada. 
# Apresente o resultado da da intercalaçõeo da primeira sequência lida com a segunda e vice-versa.

seq1 = []
seq2 = []

for i in range(5):
    seq1.append(int(input()))
for j in range(5):
    seq2.append(int(input()))

for k in range(5):
    print(seq1[k], end=' ')
    print(seq2[k], end=' ')

print()

for t in range(5):
    print(seq2[t], end=' ')
    print(seq1[t], end=' ')
    