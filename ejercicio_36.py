frutas = {'plátano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}
opc = input('¿Cuál es la fruta de la queseas saber el valor de kilos? ')
opc = opc.lower()
peso =float(input('¿Cuantos kilos quieres ?'))
if opc in frutas:
    precio = frutas.get(opc)
    resultado = precio * peso
    print(resultado,'pesos')
else:
    print('Opción no válida')
