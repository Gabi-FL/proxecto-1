import time

def escribe_despacico(frase):
    for letra in frase:    
        print(letra, end="", flush=True)
        time.sleep(0.03)
    print()

