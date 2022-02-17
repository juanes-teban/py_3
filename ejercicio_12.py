'''
Escribir un programa en Python que le pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido desde 1 hasta su edad
'''
edad = int(input('¿Cual es tu edad ?'))

for i in range(edad):
    print(f'tu edad en estos años fue {i+1} años')
