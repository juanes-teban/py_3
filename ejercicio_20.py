'''
Escribir un programa que pregunte el Nombre del Usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre en mayúsculas y <n> es el número de letras que tiene el nombre.
'''
nombre = input('¿Cómo te llamas? ')
n = len(nombre)

print(f'Hola {nombre} tu nombre tiene {n} letras')
