import random

computadora = (random.choice(["piedra", "papel", "tijera"]))



#Jugadores
jugador = (input("Escribe tu opción: "))
if jugador == "piedra" or jugador == "papel" or jugador == "tijera" :
    print("Empieza el juego")
    print("Computadora eligió:" , computadora)
    #Empate
    if jugador == computadora:
        print("Empate")

    #Ganaste
    elif jugador == "piedra" and computadora == "tijera":
        print("Ganaste!")
    elif jugador == "tijera" and computadora == "papel":
        print("Ganaste!")
    elif jugador == "papel" and computadora == "piedra":
        print("Ganaste!")

    #Perdiste      
    else:
        print("Perdiste")    
else:
    print("Debe escribir una de las opciones: piedra-papel-tijera")








