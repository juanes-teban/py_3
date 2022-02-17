'''
ejercicio_6.py
scipt en Python que le pida un número al usuario para que la computadora intente adivinarlo.
'''
import random

def numero_computadora(x):

    print("============================")
    print('¡Binvenido(a) al Juego!')
    print("============================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion= random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior

        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta regresa (A). Si es muy baja ingresa(B). Si es correcta, ingresa (C) ").lower()

    if respuesta == "a":
        limite_superior = prediccion - 1

    elif respuesta == "b":
        limite_inferior = prediccion + 1
    else:
        print(f'''!La computadora adivino tu numero correctamente:  {prediccion}¡''')


numero_computadora(10)
