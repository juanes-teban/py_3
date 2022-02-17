'''
script en Python que realice una lista de productos de un supermercado los cuales estan cducados, a punto de caducar y listos para el consumo.El programa finalizara hata que el usuario lo desee.
'''
import os
#fecha_caducación_manzana
DIA_CADUCACION_MANZANA:10
MES_CADUCACION_MANZANA:6
AÑO_CADUCACION_MANZANA:2021
#fecha_caducación_arroz
DIA_CADUCACION_ARROZ:11
MES_CADUCACION_ARROZ:7
AÑO_CADUCACION_ARROZ:2022
#fecha_caducación_lentejas
DIA_CADUCACION_LENTEJAS:9
MES_CADUCACION_LENTEJAS:7
AÑO_CADUCACION_LENTEJAS:2022
#fecha_caducacion_frijoles
DIA_CADUCACION_FRIJOLES:10
MES_CADUCACION_FRIJOLES:6
AÑO_CADUCACION_FRIJOLES:2022
#fecha_caducacion_limon
DIA_CADUCACION_LIMON:26
MES_CADUCACION_LIMON:6
AÑO_CADUCACION_LIMON:2021
#productos
MANZANA = 1
ARROZ = 2
LENTEJAS = 3
FRIJOLES = 4
LIMON = 5
SALIR = 99
def menu():
    print(f''''    Lista de supermercado
{MANZANA}) Manazana
{ARROZ}) Arroz
{LENTEJAS}) Lentejas
{FRIJOLES}) Frijoles
{LIMON}) Limon
{SALIR}) Salir
''')
def main():
    continuar =True
    while continuar:
        os.system('cls')
        menu()
        opc = int(input('¿De que producto quieres saber la fecha de caducidad?'))
        os.system('cls')
    if opc == 1:
        print(f'''la manzana dia:{DIA_CADUCACION_MANZANA} mes:{MES_CADUCACION_MANZANA} año:{AÑO_CADUCACION_MANZANA}''')

    elif opc == 2:

        print(f''''Arroz dia:{DIA_CADUCACION_ARROZ}
        mes:{MES_CADUCACION_ARROZ}
        año: {AÑO_CADUCACION_ARROZ}''')
    elif opc == 3:
        print(f''''Lentejas dia:{DIA_CADUCACION_LENTEJAS}
        mes:{MES_CADUCACION_LENTEJAS}
        año:{AÑO_CADUCACION_LENTEJAS}''')

    elif opc == 4:

        print(f'''Frijoles
        dia:{DIA_CADUCACION_FRIJOLES}
        mes:{MES_CADUCACION_FRIJOLES}
        año:{AÑO_CADUCACION_FRIJOLES}
        ''')

    elif opc == 5:

        print(f'''Limones
        dia:{DIA_CADUCACION_LIMON}
        mes:{MES_CADUCACION_LIMON}
        año:{AÑO_CADUCACION_LIMON}
        ''')

    elif opc == 99:
        print('Nos vemos...')
        continuar = False
    else:
        print('Opción no válida')
        input('presiona enter para continuar')
if __name__=='__main__':
    main()
