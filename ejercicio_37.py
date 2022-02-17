año =int(input('En que año estas: '))
dia = int(input('Escribe el número del día en el mes en el que estas '))
fecha.setdefault(año,dia)
fecha = {'dia': dia, 'mes':['Enero','Febrero','Marzo','Abril','Mayo','Junio', 'Julio','Agosto','Septiembre', 'Octubre', 'Noviembre','Diciembre'], 'año': año}
calendario = fecha.get(dia)
