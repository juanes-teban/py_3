'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la voc al introcida en mayúscula.
'''

frase = input('Introduce una frase: ')
vocal = input('Introduce una vocal: ')
print(frase.replace(vocal, vocal.upper()))
#print(frase, vocal.upper())
