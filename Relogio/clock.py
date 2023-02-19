import os
from datetime import datetime
from playsound import playsound
import time 

clear = lambda: os.system('cls')
contador = 0

while(True):
    escolha = input("\n1- Relogio (Real time)\n2- Temporizador\n3- Alarme\n4- Sair\n\nOpção: ")
    if (escolha == "1"):
        print("Relogio (Real time)\n")
        while(True):
            horas = datetime.now()
            tempoAtual = horas.strftime("%H:%M:%S")
            print("Horas: ", tempoAtual)
            clear()

    elif (escolha == "2"):
        temporizador = input("Temporizador (ex: 00:00:00 horas-minutos-segundos)\nTempo: ")

        try:
            hora = int(temporizador[0:2])
            minuto = int(temporizador[3:5])
            segundo = int(temporizador[6:8])

        
            if(hora > 24) or (minuto > 60) or (segundo >60 ):
                print("\nO limite de horas utrapassado.\nHoras até 24\nMinutos até 60\nSegundos até 60")

            else:
                
                    while(hora != 0) or (minuto !=0) or (segundo !=0):
                        print(f"{hora}:{minuto}:{segundo}")
                        segundo -= 1
                        if(segundo <= 0) and (minuto != 0):
                            segundo = 59
                            minuto -= 1
                            if(minuto <= 0) and (hora != 0):
                                minuto = 59
                                hora -=1
                        time.sleep(1)
                        clear()
        except:
            print("\nCaracter invalido, tente novamente")


    elif (escolha == "3"):

        horaDoAlarme = input("Horario do Alarme (ex: 00:00:00 horas-minutos-segundos)\nTempo: ")

        try:
            hora = int(horaDoAlarme[0:2])
            minuto = int(horaDoAlarme[3:5])
            segundo = int(horaDoAlarme[6:8])

            if(hora > 24) or (minuto > 60) or (segundo > 60 ):
                print("\nO limite de horas utrapassado.\nHoras até 24\nMinutos até 60\nSegundos até 60")

            else:
                while(True):
                    horas = datetime.now()
                    tempoAtual = horas.strftime("%H:%M:%S")

                    if(horaDoAlarme == tempoAtual):
                        print("Alarme")
                        playsound('songs/<NOME DA MUSICA>.mp3')
                        break;
                    else:
                        continue
                
        except:
            print("\nCaracter invalido, tente novamente")

        

    elif (escolha == "4"):
        break;

    else:
        print("Opção inválida, tente novamente.")