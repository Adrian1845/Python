#super
class persona():

	def __init__(self, nombre, edad, hogar):
		self.nombre=nombre
		self.edad=edad
		self.hogar=hogar

	def descripción(self):
		print("Nombre: ",self.nombre,"\nEdad: ",self.edad,
			"\nLugar de residencia: ",self.hogar)

class empleado(persona):

	def __init__(self, salario, antiguedad):
			#super() hace que se ejecuten primero los parámetros de arriba
		super().__init__("Antonio", 45, "Valdemoro")
		self.salario=salario
		self.antiguedad=antiguedad


Antonio=empleado(3500, "3 años")
Antonio.descripción()
print("---------------------------------------------------------------------------------------")
class persona():

	def __init__(self, nombre, edad, hogar):
		self.nombre=nombre
		self.edad=edad
		self.hogar=hogar

	def descripcion(self):
		print("Nombre: ",self.nombre,"\nEdad: ",self.edad,
			"\nLugar de residencia: ",self.hogar)

class empleado(persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, hogar_empleado):
		#super() hace que se ejecuten primero los parámetros de arriba
		super().__init__(nombre_empleado, edad_empleado, hogar_empleado)
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		#usamos super para apropiarnos del método descripción
		super().descripcion()
		print("Salario: ",self.salario,"\nAntigüedad: ",self.antiguedad,)

Mónica=empleado(3500, "3 años","Mónica",17,"Seseña Viejo")
Mónica.descripcion()
#isinstance nos indica si pertence o no a una clase, True or False
print(isinstance(Mónica, empleado))
Antonio=persona("Antonio",20,"Valdemoro")
print(isinstance(Antonio, empleado))