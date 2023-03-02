lista = []

for i in range(3):
    itemDaLista = float(input())
    lista.append(itemDaLista)

pi = 3.14159
print(f'TRIANGULO: {(lista[0] * lista[2]/ 2):.3f}')
print(f'CIRCULO: {(pi * lista[2]**2):.3f}')
print(f'TRAPEZIO: {((lista[0] + lista[1]) *lista[2] / 2):.3f}')
print(f'QUADRADO: {(lista[1] **2):.3f}')
print(f'RETANGULO: {(lista[0] * lista[1]):.3f}')

# lista[0] -> a
# lista[1] -> b
# lista[2] -> c
