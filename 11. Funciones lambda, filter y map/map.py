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
empleado("Juan", "Director", 6700),
empleado("Ana", "Presidenta", 7500),
empleado("Sara", "Secretaria", 2100),
empleado("Pedro", "Conserje", 2150)
]

def calculo_comision(empleado):

	if empleado.salario<=3000:
		
		empleado.salario=empleado.salario*1.03

	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for i in listaEmpleadosComision:
	print(i)