xa1, xa2, xb1, xb2 = map(int, input().split())
ya1, ya2, yb1, yb2 = map(int, input().split())

if ((xb1 > xa1) or (xb2 < xa1) or (yb1 > ya2) or (yb2 < ya1)):
    print("Não colidem")
else:
    print("Colidem")