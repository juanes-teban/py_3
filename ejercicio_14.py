'''
Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés anual y el número de años, muestre por pantalla el capital obteniodo en la inversión cada año que dura la inversión
'''


inversion = float(input('¿Cual es la cantidad a invertir? '))
esperado = float(input('Interes anual: '))
tiempo = int(input('¿Por cuantos años es la inversión?'))
capital = inversion*2


for i in range(tiempo):
     print(f'inversión dada por usted {inversion}')
     print(f'Capital aspirado ha recibir: {esperado}')
     print(f'Años de duración: {tiempo}')
     print(f'Su dinero durante los años estipulados es {capital}')
     print('*'*50)
