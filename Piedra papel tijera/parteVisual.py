import time

def escribe_despacico(frase):       #Escribe una cadena de caracteres letra a letra con un delay entre letras
    for letra in frase:    
        print(letra, end="", flush=True)
        time.sleep(0.03)
    print()

