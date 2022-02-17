'''
ejercicio_4.py
script en Python que funcione como el juego mad libs que conciste en concantenar espacios en blaco para formar una historia loca.
'''
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo en (Plural): ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} conmigo y tus {sustantivo_plural}!"

print(madlib)
