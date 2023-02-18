import random

escolhasDeDados = {}

print("\nOlá seja bem ao Dado virtual!\nEscolha o seu dado:\n")
dadoLados = 4
for item in range(1, 7):
    print(f"{item} - Dado de {dadoLados} lados")
    escolhasDeDados[item] = dadoLados
    dadoLados +=2 
    if (dadoLados == 14):
        dadoLados = 20
    
escolha= int(input("\nEscolha: "))

resultadoDado = random.randint(1, escolhasDeDados.get(escolha))

print(f"\nDado de {escolhasDeDados.get(escolha)} lados escolhido.\n\nResultado do Dado: {resultadoDado}\n")
