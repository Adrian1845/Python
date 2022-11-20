class Coche():
	#declaramos atributos iniciales/comunes
	def __init__(self):
		#encapsulamos para que no sea accesible desde fuera de la clase
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	#definimos un método
	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos
		#llamamos al chequeo interno para tener otro condicional
		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche está en marcha"
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo, no se puede arrancar"
		else:
			return "El coche está parado"
	#métodos
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", 
			self.__anchoChasis, " y un largo de ", self.__largoChasis,)
	#encapsulamos el método
	#ya que no tiene sentido hacer chequeos una vez arrancado/parado
	#AttributeError: 'Coche' object has no attribute 'chequeo_interno'
	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.galosina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.galosina=="ok" and self.aceite=="ok" and 
			self.puertas=="cerradas"):
			return True
		else:
			return False


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