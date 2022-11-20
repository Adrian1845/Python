#polimorfismo(varias formas)
class coche():
	def desplazamiento(self):
		print("Me desplazo usando cuatro ruedas")

class moto():
	def desplazamiento(self):
		print("Me desplazo usando dos ruedas")

class camion():
	def desplazamiento(self):
		print("Me desplazo usando seis ruedas")

miVehiculo=moto()
miVehiculo.desplazamiento()
miVehiculo2=coche()
miVehiculo2.desplazamiento()
miVehiculo3=camion()
miVehiculo3.desplazamiento()

print("------------------------------------------------")
class coche():
	def desplazamiento(self):
		print("Me desplazo usando cuatro ruedas")

class moto():
	def desplazamiento(self):
		print("Me desplazo usando dos ruedas")

class camion():
	def desplazamiento(self):
		print("Me desplazo usando seis ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()
#el parámetro de almacena en la función (en vehiculo)
#ahí ocurre el polimorfismo ya que miVehiculo es = a coche()
#y con la función sería: vehiculo.desplazamiento(coche())
miVehiculo=coche()

desplazamientoVehiculo(miVehiculo)