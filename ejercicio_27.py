'''
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en línea distinta.
'''
productos = input('¿Qué productos quieres ver de la cesta?')

print(productos.join(','))
