import random
import time
import os
import parteVisual
import parteLogica

contadorP = 0
contadorM = 0
continuar = True

os.system("cls" if os.name == "nt" else "clear")

parteVisual.escribe_despacico("Bienvenido al piedra papel tijera, esto es muy fácil, tú eliges qué sacar, y yo (la máquina) elijo qué sacar y a ver quien gana")

while contadorP < 3 and contadorM < 3 and continuar:
    
    time.sleep(0.3)
    parteVisual.escribe_despacico('''Escoge una opción:
        1. Piedra
        2. Papel
        3. Tijeras
        ''')

    opc_ordenador = 0
    opc_jugador = 0

    puntoM, puntoP = parteLogica.comparar_jugadas(opc_ordenador, opc_jugador)

    contadorM += puntoM
    contadorP += puntoP

    parteVisual.escribe_despacico(f'''
    Tú tienes {contadorP} puntos
    Yo tengo {contadorM} puntos
    ''')

    time.sleep(0.5)

    parteLogica.quien_gana(contadorM, contadorP)

    if contadorM ==3 or contadorP == 3:
        parteLogica.jugar_de_nuevo(contadorM, contadorP, continuar)