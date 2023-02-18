import os
from playsound import playsound

playListDeMusicas = {}

contador = 0;

pasta = 'playlist'

musicas = os.listdir(pasta)

print("\n")
print(("-")*60)
for musica in musicas:

    contador += 1

    print(contador,"-",musica)

    playListDeMusicas[contador] = musica
    
print(("-")*60)
print("\n")
escolhaMusica = int(input("Musica: "))
opcao = playListDeMusicas.get(escolhaMusica)
print('Musica '+' '+opcao+' '+'selecionda')
print('O audio está sendo reproduzido...')
playsound(pasta+'/'+opcao)

