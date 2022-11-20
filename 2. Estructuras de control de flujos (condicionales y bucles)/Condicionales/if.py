print("Evaluación")
#la variable se almacena en nota_alumno, la declaramos nosotros debido al input
nota_alumno=input("introduce la nota del alumno ")
#función
def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
#return para que nos devuelva el dato almacenado en valoracion
#print (funcion(convertir el dato de la variable > en int(variable la cual se coge el dato)))
#nota_alumno se vuelve nota
print(evaluacion(int(nota_alumno)))

#practica mía
print("practica")
nota_alumno1=input()
def evaluacion1(nota1):
	if nota1>5:
		print("aprobado")
	else:
		print("suspenso")
print(evaluacion1(int(nota_alumno1)))

#else
print("Verificación de acceso")

edad_usuario=int(input("Edad: "))
def control_de_acceso(edad):
	if edad_usuario<18:
		acceso="denegado"
	else:
		acceso="concedido"
	return acceso
print(control_de_acceso(edad_usuario))

#elif
print("Verificación de acceso")

edad_usuario=int(input("Edad: "))
def control_de_acceso(edad):
	if edad_usuario<18:
		acceso="denegado"
	elif edad_usuario>=120:
		acceso="erroneo"
	else:
		acceso="concedido"
	return acceso
print(control_de_acceso(edad_usuario))