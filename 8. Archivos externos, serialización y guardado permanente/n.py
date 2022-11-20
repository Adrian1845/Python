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
	usuarios=[]

	def agregarUsuarios (self,user):
		self.usuarios.append(user)

	def mostrarInformacion(self):
		print("Información: ")
		for i in self.usuarios:
			print(i)

listaUsuario=listaUsuarios()
nombre=str(input("Introduce el nombre: "))
genero=str(input("Introduce el género: "))
edad=int(input("Introduce la edad: "))
user=persona(nombre,genero,edad)
listaUsuario.agregarUsuarios(user)
listaUsuario.mostrarInformacion()