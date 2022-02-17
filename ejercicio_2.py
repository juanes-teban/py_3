'''
ejercicio_2.py
script en Python que le pida al usuario su edad nacionalidad para poder ingresar a una prestigiosa fiesta.
'''
import os
COLOMBIANO = 1
VENEZOLANO = 2
RUSO = 3
AMERICANO = 4
MEXICANO = 5
ESPAÑOL = 6
ALEMAN = 7
FRANCES = 8
INGLES = 9
CHILENO = 10
print(f'''             Fiesta de latinos
{COLOMBIANO}) Colombia
{VENEZOLANO}) Venezuela
{RUSO}) Rusia
{AMERICANO}) Estados Unidos
{MEXICANO}) Mexico
{ESPAÑOL}) España
{ALEMAN}) Alemania
{FRANCES}) Francia
{INGLES}) Inglaterra
{CHILENO}) Chile
''')

edad = int(input('¿Cual es tu edad?: '))
nacionalidad = int(input('¿Cual es tu nacionalidad?: '))

if nacionalidad == 1 and edad >=18:
    os.system('cls')
    print('Bienvenido, parcero')

elif nacionalidad == 2 and edad >= 18:
    os.system('cls')
    print('Bienvenido, chamo')
elif nacionalidad == 3:
    os.system('cls')
    print('Fuera de aqui')
elif nacionalidad == 4:
    os.system('cls')
    print('Larguese gringo de mierda')
elif nacionalidad == 5 and edad >= 18:
    os.system('cls')
    print('Pasale, Wey')
elif nacionalidad == 6:
    os.system('cls')
    print('Sal de aqui que te reviento')
elif nacionalidad == 7:
    os.system('cls')
    print('Fuera, Nazi de mierda')
elif nacionalidad == 8:
    os.system('cls')
    print('Largate de aqui napoleon')
elif nacionalidad == 9:
    os.system('cls')
    print('Las malvinas son argentinas, the falklands belongs to Argentina ')
elif nacionalidad == 10 and edad >=18:
    os.system('cls')
    print('Pasale, culiao')
else:
    os.system('cls')
    print('No estas invitado')


print('Nos vemos...')
