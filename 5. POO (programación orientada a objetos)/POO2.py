class Coche():
	#declaramos atributos iniciales/comunes
	def __init__(self):
		self.largoChasis=250
		self.anchoChasis=120
		#encapsulamos para que no sea accesible desde fuera de la clase
		self.__ruedas=4
		self.enmarcha=False

	#definimos un método
	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos
		if(self.enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis,
			" y un largo de ", self.largoChasis,)
miCoche=Coche()

#añadir # para cambiar el estado
print(miCoche.arrancar(True))
miCoche.estado()

print("-----------------segundo objeto-----------------")

miCoche2=Coche()
#aquí se ve la prueba del encapsulamiento 
miCoche2.__ruedas=10
print(miCoche.arrancar(False))
miCoche2.estado()