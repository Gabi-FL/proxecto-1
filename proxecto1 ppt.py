import random

def escoge_una(elección):
    match escoge_una(elección):
        case 1:
            print("piedra")
        case 2:
            print("papel")
        case 3:
            print("tijera")
    
    elección = random.randint(1, 4)
    return elección


def menu():
    print('''
    Escoge una opción
    1. Piedra
    2. Papel
    3. Tijeras''')

