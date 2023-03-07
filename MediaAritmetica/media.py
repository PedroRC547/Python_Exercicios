qntDeNotas = int(input("Qnt de notas: "))
somaNotas = 0

for i in range(qntDeNotas):
    nota = float(input(f"{i}° Nota: "))
    somaNotas += nota

mediaAritmetica = (somaNotas)/qntDeNotas
print(f"A Média Aritmética é: {mediaAritmetica:.2f}")
