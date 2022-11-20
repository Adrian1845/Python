'''def numero_par(num):

	if num % 2==0:

		return True'''

numeros=[12,234,324, 25567, 34123 ,956 ,293 ,3954]

#la funcion filter es un filtro
print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

class empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):

		return "{}, que trabaja como {}, tiene un salario de {}€.".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
empleado("Juan", "Director", 75000),
empleado("Ana", "Presidenta", 50000),
empleado("Sara", "Secretaria", 27000),
empleado("Pedro", "Conserje", 5000)
]
#condicion, parámetro a filtrar
salarios_altos=filter(lambda empleado:empleado.salario>40000, listaEmpleados)

for i in salarios_altos:

	print(i)