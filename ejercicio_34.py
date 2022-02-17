divisa = {'euro': '€', 'dolar':'$', 'yen':'Y'}
opc = input ('Escribe una divisa de la que quieras saber el simbolo: ')
opc = opc.lower()
if opc in divisa:
    print(divisa.get(opc))
else:
    print('No se encuentra esa divisa')
