import random
import time

def menu():
    print('''Escoge una opción:
    1. Piedra
    2. Papel
    3. Tijeras
    ''')

def eleccion_jugador(opcion):
    opcion =int(input("Elijo la: "))
    if opcion == 1:
        print("Has escogido piedra")
        res_jugador = 0
    elif opcion == 2:
        res_jugador = 1
        print("Has escogido papel")
    elif opcion == 3:
        res_jugador = 2
        print("Has escogido tijera")
    return res_jugador


def eleccion_maquina ():
    res_maq = random.randint(0,2)
    match res_maq:
        case 0:
            print("Yo había escogido piedra")
        case 1:
            print("Yo había escogido papel")
        case 2:
            print("Yo había escogido tijera")
    return res_maq

contadorP = 0
contadorM = 0

while not contadorP == 3:


    time.sleep(0.5)
    menu()
    time.sleep(0.5)
    opcion = 4
    opc_jugador = eleccion_jugador(opcion)
    time.sleep(0.5)
    opc_ordenador = eleccion_maquina()
    time.sleep(1)

    if opc_ordenador == (opc_jugador + 1) % 3:
        print("Ja, he ganado yo")
        contadorM += 1
    elif opc_ordenador == opc_jugador:
        print("Hemos empatado, esta no cuenta")
    else:
        print("Este punto es para ti")
        contadorP += 1

    time.sleep(1)

    if contadorM == 3:
        print("¡Has perdido! ya te dije que era el mejor en esto")
        if contadorM == 3:
            contadorM = contadorP
    elif contadorP == 3:
        print("Esta vez has ganado, ¡pero de suerte!")

        
