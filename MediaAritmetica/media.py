escolha = ''

while (escolha != '0'):

    escolha = input(
        "---Media---\n1 - Media Aritmetica (Padrão)\n2 - Media Aritmetica (Com peso)\n0 - Sair\n>>> ")

    if (escolha == '1'):
        qntDeNotas = int(
            input("\n---Media Aritmetica (Padrão)---\n\nQnt de notas: "))
        somaNotas = 0

        for i in range(qntDeNotas):
            nota = float(input(f"{i+1}° Nota: "))
            somaNotas += nota

        mediaAritmetica = (somaNotas)/qntDeNotas
        print(f"A Média Aritmética é: {mediaAritmetica:.2f}")
    elif (escolha == '2'):
        qntDeNotas = int(
            input("\n---Media Aritmetica (Com peso)---\n\nQnt de notas: "))
        somaPeso = 0
        somaNotas = 0
        for i in range(qntDeNotas):
            nota = float(input(f"{i+1}° Nota: "))
            peso = float(input(f"{i+1}° Peso: "))

            calc = (nota*peso)
            somaNotas += calc
            somaPeso += peso

            mediaAritmetica = (somaNotas)/somaPeso

            print(f"A Média Aritmética é: {mediaAritmetica:.2f}")

    elif (escolha == '0'):
        break

    else:
        print("Comando Inválido tente novamente!")
        continue
