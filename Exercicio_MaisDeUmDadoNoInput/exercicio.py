x = input("ValorUm(String) ValorDois(Int) ValorTres(Float): ")
itens = x.split()

try:
    valorUm = itens[0]  # String

    valorDois = int(itens[1])  # Int

    valorTres = float(itens[2])  # Float

    print(f"\nValorUm: {valorUm}\nValorDois: {valorDois}\nValorTres: {valorTres:.2f}")

except:
    print("Valor inválido")
