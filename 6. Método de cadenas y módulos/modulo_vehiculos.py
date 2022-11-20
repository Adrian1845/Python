try:
	class vehiculos():

		def __init__(self, marca, modelo):

			self.marca=marca
			self.modelo=modelo
			self.enmarcha=False
			self.acelera=False
			self.frena=False

		def arrancar(self):
			self.enmarcha=True
		def acelerar(self):
			self.acelera=True
		def frenar(self):
			self.frena=True

		def estado(self):
			#\n para imprimir salto de linea
	
				print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn marcha: "
					,self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: "
					,self.frena,)

	#aquí hereda la clase vehículo con todos sus métodos
	class moto(vehiculos):
		def caballito(self):
			self.hcaballito="Haciendo un caballito"
		#para sobreescribir un método debe tener el mismo nombre y los mismos argumentos	
		def estado(self):
			print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn marcha: "
				,self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: "
				,self.frena,"\nCaballito: ",self.hcaballito,)
	
	class furgoneta(vehiculos):
		def carga(self, cargar, peso):
			self.cargado=cargar
			self.kilos=peso
		def estado(self):
			print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn marcha: "
				,self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: "
				,self.frena,"\nCargado: ",self.cargado,"\nPeso: ",self.kilos,)	
	class VElectricos(vehiculos):
		def __init__(self,marca,modelo):
			super().__init__(marca,modelo)
			self.autonomia=100

		def cargarBateria(self):
			self.cargando=True
		def estado(self):		
			super().estado()
			print("Autonomía: ",self.autonomia,"\nCargando: ",self.cargando)
	#doble herencia
	class bicicletaElectrica(VElectricos, vehiculos):
		pass
except SyntaxError:
	print("f")