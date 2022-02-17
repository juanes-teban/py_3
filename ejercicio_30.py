'''
comparación de datos
'''

a = ["banano", "manzana", "Piña", "Melon"]
b = []

for i in range(len(a)):
    numero = int(input(f'cuantas frutas hay de {a[i]}: '))
    b.append(numero)
    print(a[i], b[i])
