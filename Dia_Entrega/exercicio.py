diaCompra = input()
prazoEntregua = int(input())


diasDaSemana = ['domingo', 'segunda', 'terca',
                'quarta', 'quinta', 'sexta', 'sabado']

if prazoEntregua == 0:
    print(f"sera entregue {diaCompra}")

x = diasDaSemana.index(diaCompra)
if x+prazoEntregua > 6:
    restantes = (prazoEntregua - (6 - x))-1
    localizacao = diasDaSemana[restantes]
else:
    localizacao = x+prazoEntregua
    localizacao = diasDaSemana[localizacao]
print(f"sera entregue {localizacao}")
