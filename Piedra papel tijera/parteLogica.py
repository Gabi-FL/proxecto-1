import parteVisual
import random

def eleccion_jugador() -> int|str:          #Recoge la elección del jugador y devuelve el valor a comparar con la elección de la máquina
    parteVisual.escribe_despacico("Elijo la: ")
    opcion =int(input())
    if (opcion < 4 and opcion > 0):
        if opcion == 1:
            parteVisual.escribe_despacico("Has escogido piedra")
            return 0
        elif opcion == 2:
            parteVisual.escribe_despacico("Has escogido papel")
            return 1
        else:
            parteVisual.escribe_despacico("Has escogido tijera")
            return 2
    else:
        parteVisual.escribe_despacico("Esa no era una opción, escoge otra vez")

def eleccion_maquina() -> int:      #Genera una elección de la máquina entre 0 y 2
    res_maq = random.randint(0,2)
    match res_maq:
        case 0:
            parteVisual.escribe_despacico("Yo había escogido piedra")
        case 1:
            parteVisual.escribe_despacico("Yo había escogido papel")
        case 2:
            parteVisual.escribe_despacico("Yo había escogido tijera")
    return res_maq