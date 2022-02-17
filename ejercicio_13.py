'''
Escribir que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 haste ese número separados por comas
'''

numero = int(input('¿Qué número quieres ver sus números anteriores?'))
i = 0
for i in range(numero, -1, -1):
    print(i, end = ", ")
