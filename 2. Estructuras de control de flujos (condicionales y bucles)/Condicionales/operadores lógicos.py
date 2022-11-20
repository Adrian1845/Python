#and(y si)
print("Programa de becas 2020")
distancia_escuela=int(input("Introduce la distancia a la escuela en km "))
print(distancia_escuela)

n_hermanos=int(input("Introduce el número de hermanos "))
print(n_hermanos)

salario_familiar=int(input("Introduce el salario familiar "))
print(salario_familiar)

def beca(distancia,hermanos,salario):
	if distancia_escuela>=40 and n_hermanos>2 and salario_familiar<=20000:
		print("tienes derecho a beca")
	else:
		print("no tienes derecho a beca")

print(beca(distancia_escuela,n_hermanos,salario_familiar))

#or (o si no)
def beca(distancia,hermanos,salario):
	if distancia_escuela>=40 and n_hermanos>2 or salario_familiar<=20000:
		print("tienes derecho a beca")
	else:
		print("no tienes derecho a beca")

print(beca(distancia_escuela,n_hermanos,salario_familiar))

#in (en)
print("Optativas 2020")
Optativas=["Informática gráfica, Pruebas de Software, Usabilidad y accesibilidad"]
print(Optativas)
asignatura=input("Escribe la asignatura escogida: ")

if asignatura in ("Informática gráfica", "Pruebas de Software", "Usabilidad y accesibilidad"):
	print("Has escogido: ", asignatura)
else:
	print("La asigantura escogida no está disponible")