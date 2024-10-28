import random

def jugador():
    eleccion = 1

    while eleccion >= 0 and eleccion <= 2:
        print('''
        1. Piedra
        2. Papel
        3. Tijeras''')
        opcion = int(input("Escoge una opción: "))
        return opcion

opcion = jugador()

if opcion == 1:
    print("Has escogido piedra")
    opc_jugador = 0
elif opcion == 2:
    opc_jugador = 1
    print("Has escogido papel")
elif opcion == 3:
    opc_jugador = 2
    print("Has escogido tijera")

def maquina ():
    return random.randint(0,2)

opc_ordenador = maquina()

if opc_ordenador == (opc_jugador + 1) % 3:
    print ("gana máquina")
else:
    print ("gana jugador")


#jugador()
#0 piedra, 1 papel, 2 tijeras    por lo que 1 gana a 0, 2 gana a 1 y 0 gana 2
#if opc_ordenador == (opc_usuario + 1) % 3:
    #gana ordenador