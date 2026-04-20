estado = int(input("Digite o código do estado da carga (1-5): "))
peso = int(input("Digite o peso da carga em toneladas: "))
carga = int(input("Digite o código da carga (10 - 40): "))

peso_convertido = peso * 1000

if carga >= 10 and carga <= 20:
    print("100,00 por kg")
    preco_carga = peso_convertido * 100.00

elif carga > 20 and carga <= 30:
    print("250,00 por kg")
    preco_carga = peso_convertido * 250.00

elif carga > 30 and carga <= 40:
    print("340,00 por kg")
    preco_carga = peso_convertido * 340.00

else:
    print("codigo invalido")

if estado == 1:
    imposto = preco_carga * 0.35

elif estado == 2:
    imposto = preco_carga * 0.25

elif estado == 3:
    imposto = preco_carga * 0.15

elif estado == 4:
    imposto = preco_carga * 0.05

elif estado == 5:
    imposto = 0
else:
    print("estado invalido")

preco_total  = preco_carga + imposto

print(f"Preco da carga em kilos: R$ {preco_carga:.2f}")
print(f"Preco do imposto R$ {imposto:.2f}")
print(f"Preco da carga com impostos R$ {preco_total:.2f}")