horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

salario_atual = horas * valor_hora

salario_novo = (1 + (horas ** 1.5) / (valor_hora ** 2.5)) * salario_atual

print(f"Salário Atual: R$ {salario_atual:.2f}")
print(f"Novo Salário com Bônus: R$ {salario_novo:.2f}")