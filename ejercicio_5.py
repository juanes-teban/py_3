'''
script en Python que el usuario adivine un número generado por el programa en un rango especifico y a medida que avancemos le diremos si ese numero es mayor menor o igual
'''
import random


def adivina_el_numero(x):

    print('===========================')
    print('Bienvenido(a) al juego, ')
    print('===========================')
    print('Tu meta es adivinar el numero generado por la computadora.')

    numero_aleatorio = random.randint(1, x)

    predicción = 0
    while predicción != numero_aleatorio:
        predicción = int(input(f''''¿Cual crees que sea el numero entre 1 y {x}:  ?'''))

        if predicción < numero_aleatorio:
            print('Intenta otra vez. Este número es pequeño')
        elif predicción > numero_aleatorio:
            print('Intenta otra vez. Este número es mayor.')

    print(f"¡Felicitaciones adivinaste el número {numero_aleatorio}!")


adivina_el_numero(10)
