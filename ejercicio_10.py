'''
script en Python que le pida al usuario sus datos para interactuar con el. El ejercicio debe ser implementado con un diccionario.
'''
nombre = input('¿Cómo te llamas?')
edad = int(input('¿Cuál es tu edad?'))
residencia = input('¿Cuál es tu lugar de residencia?')
telefono = int(input('¿Cuál es tu número de télefono?'))

persona = {'nombre': nombre, 'edad': edad, 'residencia':residencia, 'telefono' : telefono}

print(persona['nombre'],persona['edad'], persona['residencia'], persona['telefono'])
