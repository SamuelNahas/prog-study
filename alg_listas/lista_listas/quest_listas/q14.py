x = float(input())
seq = [x]
somatorio = x
comp = 2

for i in range(2, 16):
    termo = (comp * (x ** comp)) / (comp * comp)
    seq.append(termo)
    somatorio += termo    
    comp += 1

media = somatorio/15
termos_abaixo = 0
for j in range(len(seq)):
    print("{0:.3f}".format(seq[j]), end=" ")
    if seq[j] < media:
        termos_abaixo += 1

print()
print()
print("A média dos termos da sequência é de {0:.2f}".format(media))
if termos_abaixo == 1:
    print("Existe 1 único termo na sequência cujo valor é abaixo da média")
else:
    print('Existem {0} termos na sequência que estão abaixo da média'.format(termos_abaixo))    
