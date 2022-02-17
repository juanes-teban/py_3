curso = {'Matématicas' : 6, 'Física': 4, 'Química': 5 }

credito = 0
for asignatura, nota in curso.items():
    print(asignatura, "asignatura", nota, "nota")
    credito += nota
    print(credito, "Es el número total de créditos")
