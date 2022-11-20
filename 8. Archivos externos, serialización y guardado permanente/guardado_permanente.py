import pickle

class persona:

	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado un usuario: ",self.nombre)
	#convertir en texto
	def __str__(self):
		return"{} {} {}".format(self.nombre, self.genero, self.edad)

class listaUsuarios:
	#lista usuarios
	usuarios=[]

	#constructor para guardar usuarios en el archivo
	def __init__(self):

		listaDeUsuarios=open("guardadoPermanente","ab+")
		listaDeUsuarios.seek(0)
		try:
			self.usuarios=pickle.load(listaDeUsuarios)
			print("Se cargaron {} personas del fichero externo".format(len(self.usuarios)))
		except:
			print("el fichero está vacío")
		finally:
			listaDeUsuarios.close()
			del(listaDeUsuarios)

	def agregarUsuario(self, user):
		self.usuarios.append(user)
		self.guardarUsuarios()

	def guardarUsuarios(self):
		listaDeUsuarios=open("guardadoPermanente","wb+")
		#volcamos la información de la lista de usuarios en el archivo
		pickle.dump(self.usuarios, listaDeUsuarios)
		listaDeUsuarios.close()
		del(listaDeUsuarios)

	def mostrarInformacion(self):
		print("Información: ")
		for i in self.usuarios:
			print(i)

listaUsuario=listaUsuarios()
nombre=str(input("Introduce el nombre: "))
genero=str(input("Introduce el género: "))
edad=int(input("Introduce la edad: "))
user=persona(nombre,genero,edad)
listaUsuario.agregarUsuario(user)
listaUsuario.mostrarInformacion()


