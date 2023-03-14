nomeVendedor = input("Nome do Vendedor: ")
salarioFixo = float(input("Salario fixo: "))
totalDeVendas = float(input("Total de Vendas (Em dinheiro): "))

salario_bonus = (totalDeVendas*15)/100

total_salario = salarioFixo+salario_bonus

print(f"Total: R$ {total_salario:.f}")
