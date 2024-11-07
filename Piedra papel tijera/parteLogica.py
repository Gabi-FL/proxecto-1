import parteVisual
import random
import os
from typing import Tuple

def eleccion_jugador() -> int:          
    """Esta función pide al jugador que escoja una de las tres opciones, piedra, papel o tijera, y lo transforma en un valor 
    entero entre el 0 y el 2

    Returns:
        int: un valor entre 0 y 2 que representa la opción elegida por el jugador
    """
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
    """Esta función genera un número aleatorio entre el 0 y el 2, que será la opción elegida por la máquina

    Returns:
        int: el valor elegido aleatoriamente por la máquina
    """
    res_maq = random.randint(0,2)
    match res_maq:
        case 0:
            parteVisual.escribe_despacico("Yo había escogido piedra")
        case 1:
            parteVisual.escribe_despacico("Yo había escogido papel")
        case 2:
            parteVisual.escribe_despacico("Yo había escogido tijera")
    return res_maq


def comparar_jugadas(opc_ordenador: int, opc_jugador: int) -> Tuple[int, int]:
    """Esta función compara la elección del jugador con la de la máquina, determina quien gana y suma un punto al marcador

    Args:
        opc_ordenador (int): La elección de la máquina (es un número entre el 0 y el 2)
        opc_jugador (int): La elección del jugador (es un número entre el 0 y el 2)

    Returns:
        Tuple[int, int]: una tupla con los valores de las variables puntoJugador y puntoMaquina. Uno de los dos valores va
        a valer 1 excepto en caso de empate, que nadie obtendrá un punto
    """
    frases_ganar = ["Este punto es para ti", "Te sumamos un puntito", "Punto para ti, pero no te acostumbres"]
    frases_perder = ["Ja, he ganado yo", "Punto para mua", "Soy invencible, punto para mi"]

    puntoJugador = 0
    puntoMaquina = 0

    opc_jugador = 3
         #llama a la función elección máquina si la primera vez el valor es incorrecto
    opc_jugador = eleccion_jugador()

    opc_ordenador = eleccion_maquina()

    if opc_ordenador == (opc_jugador + 1) % 3:         
        parteVisual.escribe_despacico(random.choice(frases_perder))
        puntoMaquina = 1
    elif opc_ordenador == opc_jugador:
        parteVisual.escribe_despacico("Hemos empatado, esta no cuenta")
    else:
        parteVisual.escribe_despacico(random.choice(frases_ganar))
        puntoJugador = 1
        
    return puntoMaquina, puntoJugador

def quien_gana(contadorM: int, contadorP: int) -> None:
    """Esta función imprime un mensaje indicando quien ha ganado la partida

    Args:
        contadorM (int): la puntuación de la máquina
        contadorP (int): la puntuación del jugador
    """
    if contadorM == 3:
        parteVisual.escribe_despacico("¡Has perdido! ya te dije que era el mejor en esto")
    elif contadorP == 3:
        parteVisual.escribe_despacico("Esta vez has ganado, ¡pero de suerte!")

def jugar_de_nuevo(contadorM:int, contadorP: int, continuar: bool) -> Tuple[int, int, bool]:
    """Esta función da la opción de volver a jugar otra partida

    Args:
        contadorM (int): la puntuación de la máquina
        contadorP (int): la puntuación del jugador
        continuar (bool): una bandera que indica si se sigue jugando o no

    Returns:
        Tuple[int, int, bool]: los valores anteriores; en caso de que se juegue otra partida los
        contadores se devuelven a 0 y la bandera con valor True, si no la bandera va con valor False
    """
    parteVisual.escribe_despacico("Volver a jugar? si/no")
    volver_a_jugar = input()
    if volver_a_jugar.lower() == "si":
        contadorM = 0
        contadorP = 0
        os.system("cls" if os.name == "nt" else "clear")
        return contadorP, contadorM, continuar
    else:
        continuar = False
        return contadorP, contadorM, continuar

    
        
