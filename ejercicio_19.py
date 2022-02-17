'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido
'''
#Solución 1
'''nombre = input('¿Cómo te llamas: ?')

numero = int(input('Introduce un número: '))

for i in range(numero):
    print(nombre)'''

#Solución 2

nombre = input('¿Cómo te llamas: ?')
n = int(input('Introduce un número: '))
print((nombre + "\n") * (n))
