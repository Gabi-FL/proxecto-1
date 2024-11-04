import random
import time
import os
import parteVisual
import parteLogica

contadorP = 0
contadorM = 0

os.system("cls" if os.name == "nt" else "clear")

parteVisual.escribe_despacico("Bienvenido al piedra papel tijera, esto es muy fácil, tú eliges qué sacar, y yo (la máquina) elijo qué sacar y a ver quien gana")

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
    comparar_jugadas(opc_ordenador, opc_jugador)


    parteVisual.escribe_despacico(f'''
    Tú tienes {contadorP} puntos
    Yo tengo {contadorM} puntos
    ''')

    time.sleep(0.5)

    if contadorM == 3:
        parteVisual.escribe_despacico("¡Has perdido! ya te dije que era el mejor en esto")
    elif contadorP == 3:
        parteVisual.escribe_despacico("Esta vez has ganado, ¡pero de suerte!")

    if contadorM ==3 or contadorP == 3:         #ofrece la opción de jugar otra partida o de acabar de jugar
        parteVisual.escribe_despacico("Volver a jugar? si/no")
        volver_a_jugar = input()
        if volver_a_jugar.lower() == "si":
            contadorM = 0
            contadorP = 0
            os.system("cls" if os.name == "nt" else "clear")
        else:
            break