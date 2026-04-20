a = int(input("digite o valor do lado a: "))
b = int(input("digite o valor do lado b: "))
c = int(input("digite valor do lado c: "))

a, b, c = sorted([a, b, c], reverse=True)


if a < b + c:

    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOCELES")

else:
    print("NAO FORMA TRIANGULO")