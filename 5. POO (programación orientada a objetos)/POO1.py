class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

	#definimos un método
	def arrancar(self):
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"
miCoche=Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")

#añadir # para cambiar el estado
miCoche.arrancar()
print(miCoche.estado())

print("segundo objeto")

miCoche2=Coche()
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
print(miCoche2.estado())