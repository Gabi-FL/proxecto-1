import parteVisual
import random

def eleccion_jugador():
    parteVisual.escribe_despacico("Elijo la: ")
    opcion =int(input())
    if opcion == 1:
        parteVisual.escribe_despacico("Has escogido piedra")
        return 0
    elif opcion == 2:
        parteVisual.escribe_despacico("Has escogido papel")
        return 1
    elif opcion == 3:
        parteVisual.escribe_despacico("Has escogido tijera")
        return 2


def eleccion_maquina ():
    res_maq = random.randint(0,2)
    match res_maq:
        case 0:
            parteVisual.escribe_despacico("Yo había escogido piedra")
        case 1:
            parteVisual.escribe_despacico("Yo había escogido papel")
        case 2:
            parteVisual.escribe_despacico("Yo había escogido tijera")
    return res_maq

