peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso/(altura*altura)

print("IMC: {:.2}".format(imc))

if (imc < 18.5):
    print("Abaixo do peso normal")
elif (imc >= 18.5) and (imc <= 24.9):
    print("Peso normal")
elif (imc >= 25.0) and (imc <= 29.9):
    print("Excesso de peso")
elif (imc >= 30.0) and (imc <= 34.9):
    print("Obesidade classe I")
elif (imc >= 35.0) and (imc <= 39.9):
    print("Obesidade classe II")
else:
    print("Obesidade classe III")