'''
script en Python que le pide al usuario un numero del 1 al 32 para indicar la capital del departamento que quiere conocer
'''



print(''''         Capitales de Colombia
1) Amazonas
2) Antioquia
3) Arauca
4) Atlántico
5) Bolívar
6) Boyacá
7) Caldas
8) Caquetá
9) Casanare
10) Cauca
11) Cesar
12) Chocó
13) Córdoba
14) Cundinamarca
15) Guainía
16) Guaviare
17) Huila
18) La Guajira
19) Magdalena
20) Meta
21) Nariño
22) Norte de Santander
23) Putumayo
24) Quindío
25) Risaralda
26) San Andrés y Providencia
27) Santander
28) Sucre
29) Tolima
30) Valle del Cauca
31) Vaupés
32) Vichada
''')
departamento = int(input('¿De que departamento quieres ver la capital?'))

if departamento == 1:
    print(' La capital del Amazonas es Leticia')
elif departamento == 2:
    print('La capital de Antioquia es Medellin')
elif departamento == 3:
    print('La capital de Arauca es Arauca')
elif departamento == 4:
    print('La capital del Atlantico es Barranquilla')
elif departamento == 5:
    print('La capital de Bolivar es Cartagena de Indias')
elif departamento == 6:
    print('La capital de Boyaca es Tunja')
elif departamento == 7:
    print('La capital de Caldas  es Manizales')
elif departamento == 8:
    print('La capital de Caquetá  es Florencia ')
elif departamento == 9:
    print('La capital de Casanare  es Yopal ')
elif departamento == 10:
    print('La capital de Cauca es Popayán ')
elif departamento == 11:
    print('La capital de Cesar es Valledupar ')
elif departamento == 12:
    print('La capital de Chocó es Quibdó ')
elif departamento == 13:
    print('La capital de Córdoba es Montería ')
elif departamento == 14:
    print('La capital de Cundinamarca es Bogotá ')
elif departamento == 15:
    print('La capital de Guainía es Inírida')
elif departamento == 16:
    print('La capital de  Guaviare es San José del Guaviare')
elif departamento == 17:
    print('La capital de Huila es Neiva ')
elif departamento == 18:
    print('La capital de La Guajira es Riohacha')
elif departamento == 19:
    print('La capital de  Magdalena es Santa Marta')
elif departamento == 20:
    print('La capital de Meta es Villavicencio')
elif departamento == 21 :
    print('La capital de Nariño es San Juan de Pasto')
elif departamento == 22:
    print('La capital de Norte de Santander es San José de Cúcuta')
elif departamento == 23:
    print('La capital de Putumayo es Mocoa')
elif departamento == 24:
    print('La capital de Quindío es Armenia')
elif departamento == 25:
    print('La capital de Risaralda es Pereira')
elif departamento == 26:
    print('La capital de San Andrés y Providencia es San Andrés')
elif departamento == 27:
    print('La capital de Santander es Bucaramanga')
elif departamento == 28:
    print('La capital de Sucre es Sincelejo')
elif departamento == 29:
    print('La capital de Tolima es Ibagué')
elif departamento == 30:
    print('La capital de Valle del Cauca es Cali')
elif departamento == 31:
    print('La capital de Vaupés es Mitú')
elif departamento == 32:
    print('La capital de Vichada es Puerto Carreño')
else:
    print('Esa opcion no existe')


print('Nos vemos...')
