'''
Los teléfonos tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34-913724710-56. Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin prefijo y la extensión
'''
numero = int(input('Inroduce el número: '))
print('El número de teléfono es:' numero[4:-3])
