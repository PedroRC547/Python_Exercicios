nome= input("Qual nome do paciente?")
idade = int(input("Qual e idade do paciente?"))
doencas = input("O paciente tem asma/diabetes/etc?").upper() # S ou N
sintomas = input("O paciente apresenta sintomas?").upper() # S ou N

# Corona < 15 r > 60

if idade <= 15 or idade >= 60:
    riscoidade = "S"
else:
    riscoidade = "N"

if riscoidade == "S" and doencas == "S" and sintomas == "S":
    print("O paciente tem atendimento prioritario e vai para UTI")

elif riscoidade == "S" and doencas == "S" and sintomas == "N":
    print("O paciente tem atendimento prioritario e vai para quarentena")

elif riscoidade == "S" and doencas == "N" and sintomas == "S":
    print("O paciente tem atendimento prioritario e vai para quarentena")

elif riscoidade == "N" and doencas == "N" and sintomas == "S":
    print("Observacao em casa!!!")

elif riscoidade == "S" and doencas == "N" and sintomas == "N":
    print("partiu NETFLIX!!!")

else:
    print("partiu NETFLIX!!!")