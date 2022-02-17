'''
ejercicio_8.py
script en Python que genere un juego como "el ahorcado" donde el usuario adivine una palabra letra por letra
'''
import random
import string

from palabras import palabras


def obtener_palabra_valida(lista_palabras):

     palabra = random.choice(palabras)
     while '-' in palabra or ' ' in palabra:
          palabra = random.choice(palabras)

     return palabra.upper()


def ahorcado():

    print("=============================")
    print("¡Bienvenido al juego del ahorcado!")
    print("=============================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vida = 7

    while len(letras_por_adivinar) > 0 and vidas >  0 :
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        palabra_lista =[letra if letra in letras_adivinadas else '_' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palbra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas-1
                print(f"\nLa letra no esta en la palabra ")
        elif letra_usuario in letras_adivinadas:
              print("\n Ya escogiste esta letra. Por favor escoge una letra nueva")
        else:
              print("\nEsta letra no es valida")
    if vidas == 0:
        print(vidas_diccionario_visual)
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. la palabra era: {palabra}")
    else:
        print(f"Excelente adivinaste la palabra {palabra}")


ahorcado()
