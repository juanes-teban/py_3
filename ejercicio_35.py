
persona = {}
def agregar_nombre(persona):
    print('''  Escribe tu nombre, edad, dirección. teléfono''')
    nombre = input('¿Cómo te llamas? ')
    telefono = int(input('¿Cuál es tu número de teléfono? '))
    edad = int(input('¿Cuál es tu edad? '))
    direccion = input('¿Cuál es tu dirección? ')
    persona.setdefault(nombre, (telefono, edad, direccion))
    if len(persona) > 0:
        for individuo,datos in persona.items():
            print(f'Nombre: {individuo}')
            print(f'Telefono: {datos[0]}')
            print(f'edad: {datos[1]}')
            print(f'dirección: {datos[2]}')




agregar_nombre(persona)
