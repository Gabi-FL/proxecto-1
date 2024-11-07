import time

def escribe_despacico(frase: str) -> None:    
    """Esta función recibe una cadena de caracteres y la escribe letra a letra con un delay entre letras

    Args:
        frase (str): La frase que va a escribir
    """
    for letra in frase:    
        print(letra, end="", flush=True)
        time.sleep(0.0)         #hay que poner 0.03 en el valor de time.sleep después de probar
    print()

