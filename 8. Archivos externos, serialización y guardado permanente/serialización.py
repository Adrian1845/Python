#serializar es guardar un fichero externo codificado en binario
#serializar colecciones
import pickle

lista_nombres=["Andrea","Yaiza","Mónica","Rocío"]

fichero_binario=open("ejemplo_serializacion","wb")#escritura binariaº

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()
#borrarlo de la memoria
del fichero_binario


fichero=open("ejemplo_serializacion","rb")#leer binario

lista=pickle.load(fichero)
print(lista)

fichero.close()
#serializar objetos
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
coche1=vehiculos("Mazda","XR5")
coche2=vehiculos("Seat","Ateca")
coche3=vehiculos("Renault","Megane")

coches=[coche1, coche2, coche3]

fichero=open("serializar_objetos", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

fichero=open("serializar_objetos","rb")

cocheS=pickle.load(fichero)
fichero.close()
del(fichero)

for i in cocheS:
	print(i.estado())