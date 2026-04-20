import sys

def calculo_parcelas(valor_parcelas):
    if valor_parcelas >= 3 and valor_parcelas <= 6:
        return 0.05
    elif valor_parcelas >= 7 and valor_parcelas <= 12:
        return 0.08
    elif valor_parcelas >= 13 and valor_parcelas <= 24:
        return 0.1
    else:
        print("Parcelas Inválidas")
        sys.exit()

def pode_aprovar(idade, valor_parcelas, renda_mensal):
    if idade >= 18 and valor_emprestimo <= renda_mensal * 20:
        calculo_parcelas(valor_parcelas)
    else:
        print("Emprestimo NEGADO")
        sys.exit()

def formula_valor_parcelas(valor_emprestimo, taxa_juros, valor_parcelas):
    return valor_emprestimo * (taxa_juros * (1 + taxa_juros)**valor_parcelas) / ((1 + taxa_juros)**valor_parcelas - 1)

def total_pago(valor_total_parcelas, valor_parcelas):
    return valor_total_parcelas * valor_parcelas

def juros_pagos(total_de_parcelas, valor_emprestimo):
    return total_de_parcelas - valor_emprestimo

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do emprestimo: "))
valor_parcelas = int(input("Digite o valor da parcela (3x - 24x): "))

pode_aprovar(idade, valor_parcelas, renda_mensal)

taxa_juros = calculo_parcelas(valor_parcelas)

valor_total_parcelas = formula_valor_parcelas(valor_emprestimo, taxa_juros, valor_parcelas)
total_de_parcelas = total_pago(valor_total_parcelas, valor_parcelas)
juros = juros_pagos(total_de_parcelas, valor_emprestimo)

print("============Resultado============")
print(f"Nome: {nome}")
print(f"Serão {valor_parcelas} Parcelas de: R$ {valor_total_parcelas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"A taxa de juros mensais aplicada: {taxa_juros * 100:.2f}%")
print(f"Valor total pago: R$ {total_de_parcelas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Total de juros: R$ {juros:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))