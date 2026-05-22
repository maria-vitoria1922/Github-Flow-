a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Nao existem raizes reais")

elif delta == 0:
    x = -b / (2*a)
    print("x =", x)

else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)

    print("x1 =", x1)
    print("x2 =", x2)
