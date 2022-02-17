person = {}
continuar = True
while continuar:
    opc = input('¿Qué dato personal quieres ingresar? ')
    contenido = input(f'Dime tu {opc} ')
    person[opc] = contenido
    print(person)
    continuar =input('¿Quieres coninuar (Si/No)?') == "Si"
