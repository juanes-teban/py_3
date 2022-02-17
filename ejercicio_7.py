'''
script en Python que juegue piedra papel o tijeras con el usuario, el programa escogera una opción al azar al igual que el usuario se necesitara una entrada para que elusuario pueda interactuar con el juego
'''
import random


def jugar():
    usuario = input("¡Escoge una opción: 'pi'para piedra, 'pa'para papel, 'ti' para tijera!.\n").lower()
    computadora = random.choice(['pi','pa','ti'])
    print(f'la computadora escogio {computadora}')
    if usuario == computadora:
        return '¡Empate!'
    if gano_el_jugador(usuario,computadora):
        return '¡Ganaste!'

    return "¡Perdiste!"


def gano_el_jugador(jugador,oponente):
    if((jugador =='pi'and oponente == 'ti')
     or(jugador =='pa'and oponente == 'pi')
     or(jugador =='ti' and oponente =='pa' )):
     return True
    else:
     return False



print(jugar())
