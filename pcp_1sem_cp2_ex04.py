def calcular_horas_extras(salario_base, horas):
    return horas * (salario_base * 0.015)

def calcular_descontos_faltas(salario_base, faltas):
    return faltas * (salario_base * 0.02)

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "s":
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0


nome = input("Digite seu nome: ")
cargo = int(input("Digite seu cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario = float(input("Digite seu salario: "))
horas = int(input("Digite a quantidade de horas extras trabalhadas: "))
faltas = int(input("Digite a quantidade de faltas no mes: "))
bonus = input("Recebeu bonus por desempenho? (s/n): ").lower()

hora_extra = calcular_horas_extras(salario, horas)
total_desconto = calcular_descontos_faltas(salario, faltas)
cargo_bonus = calcular_bonus(cargo, bonus)

total_de_acrescimo = hora_extra + cargo_bonus
salario_bruto = salario
salario_final = salario_bruto + total_de_acrescimo - total_desconto

print("\n--- Resultado ---")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Total de acréscimos: R$ {total_de_acrescimo:.2f}")
print(f"Total de descontos: R$ {total_desconto:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")