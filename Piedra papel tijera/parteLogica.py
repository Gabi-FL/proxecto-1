import parteVisual
import random


def eleccion_jugador() -> int:          
    '''
    Recoge la elección del jugador y devuelve el valor a comparar con la elección de la máquina
    '''
    parteVisual.escribe_despacico("Elijo la: ")

    opcion = ""
    valor = 0
    opciones_validas = ("1", "2", "3")

    while (opcion not in opciones_validas):
        opcion =input()
        if opcion == "1":
            parteVisual.escribe_despacico("Has escogido piedra")
            valor = 0
        elif opcion == "2":
            parteVisual.escribe_despacico("Has escogido papel")
            valor = 1
        elif opcion == "3":
            parteVisual.escribe_despacico("Has escogido tijera")
            valor = 2
        else:
            parteVisual.escribe_despacico("Esa no era una opción, escoge otra vez")
    return valor


def eleccion_maquina() -> int:      
    '''
    Genera una elección de la máquina entre 0 y 2
    '''
    res_maq = random.randint(0,2)
    match res_maq:
        case 0:
            parteVisual.escribe_despacico("Yo había escogido piedra")
        case 1:
            parteVisual.escribe_despacico("Yo había escogido papel")
        case 2:
            parteVisual.escribe_despacico("Yo había escogido tijera")
    return res_maq


def comparar_jugadas(opc_ordenador, opc_jugador): -> 
    '''
    Compara la elección del jugador con la de la máquina, determina quien gana y suma un punto al marcador
        '''
    frases_ganar = ["Este punto es para ti", "Te sumamos un puntito", "Punto para ti, pero no te acostumbres"]
    frases_perder = ["Ja, he ganado yo", "Punto para mua", "Soy invencible, punto para mi"]

    contadorP = 0
    contadorM = 0

    if opc_ordenador == (opc_jugador + 1) % 3:         
        parteVisual.escribe_despacico(random.choice(frases_perder))
        contadorM += 1
    elif opc_ordenador == opc_jugador:
        parteVisual.escribe_despacico("Hemos empatado, esta no cuenta")
    else:
        parteVisual.escribe_despacico(random.choice(frases_ganar))
        contadorP += 1