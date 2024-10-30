import random
import time
import os
import parteVisual
import parteLogica

contadorP = 0
contadorM = 0

os.system("cls" if os.name == "nt" else "clear")

while contadorP < 3 or contadorM < 3:
    
    time.sleep(0.3)
    parteVisual.escribe_despacico('''Escoge una opción:
        1. Piedra
        2. Papel
        3. Tijeras
        ''')
    time.sleep(0.3)
    opc_jugador = parteLogica.eleccion_jugador()
    time.sleep(0.3)
    opc_ordenador = parteLogica.eleccion_maquina()
    time.sleep(0.3)
    frases_ganar = ["Este punto es para ti", "Te sumamos un puntito", "Punto para ti, pero no te acostumbres"]
    frases_perder = ["Ja, he ganado yo", "Punto para mua", "Soy invencible, punto para mi"]

    if opc_ordenador == (opc_jugador + 1) % 3:
        parteVisual.escribe_despacico(random.choice(frases_perder))
        contadorM += 1
    elif opc_ordenador == opc_jugador:
        parteVisual.escribe_despacico("Hemos empatado, esta no cuenta")
    else:
        parteVisual.escribe_despacico(random.choice(frases_ganar))
        contadorP += 1

    parteVisual.escribe_despacico(f'''
    Tú tienes {contadorP} puntos
    Yo tengo {contadorM} puntos
    ''')

    time.sleep(0.5)

    if contadorM == 3:
        parteVisual.escribe_despacico("¡Has perdido! ya te dije que era el mejor en esto")
    elif contadorP == 3:
        parteVisual.escribe_despacico("Esta vez has ganado, ¡pero de suerte!")

    if contadorM ==3 or contadorP == 3:
        parteVisual.escribe_despacico("Volver a jugar? si/no")
        volver_a_jugar = input()
        if volver_a_jugar.lower() == "si":
            contadorM = 0
            contadorP = 0
            os.system("cls" if os.name == "nt" else "clear")
        else:
            break