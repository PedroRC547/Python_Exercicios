import string
import random


caracteresEspeciais = ['@', '$', '&']
caracteresBase = []
contador = 0
senha = ''

palavraBase = input("Palavra base: ")
qntCaracteres = int(input("Quantos caracteres: "))

for car in range(len(palavraBase)):
    caracteresBase.append(palavraBase[car])

while (qntCaracteres != contador):
    contador += 1
    opcao_um = [random.choice(string.ascii_letters),
                str(random.randint(0, 9)), random.choice(caracteresEspeciais)]

    aleatorioBase = [random.choice(opcao_um), random.choice(caracteresBase)]

    caracter = random.choice(aleatorioBase)
    senha += caracter

print("Senha sugerida: ", senha)
