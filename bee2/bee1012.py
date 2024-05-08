a = float(input())
b = float(input())
c = float(input())

def areaTriangulo(a, c):
    return (a*c)/2

def areaC(c):
    return (3.14159 * (c**2))

def areaTrapezio(a, b, c):
    return ((a+b)*c)/2

def areaQ(b):
    return (b*b)

def areaR(a, b):
    return (a*b)

print("TRIANGULO: {:.3f}".format(areaTriangulo(a, c)))
print("CIRCULO:  {:.3f}".format(areaC(c)))
print("TRAPEZIO: {:.3f}".format(areaTrapezio(a , b, c)))
print("QUADRADO: {:.3f}".format(areaQ(b)))
print("RETANGULO: {:.3f}".format(areaR(a, b)))