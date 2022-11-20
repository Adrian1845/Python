print("ejercicio 1")

num1=int(input("n1 "))
num2=int(input("n2 "))

def DevuelveMax(n1, n2):
	if n1>n2:
		print("n1 es mayor")
	elif n1<n2:
		print("n2 es mayor")
	else:
		print("los números son iguales")

print(DevuelveMax(num1, num2))

print("ejercicio 2")

name=input("Nombre: ")
direc=input("Dirección: ")
tfno=(int(input("Teléfono: ")))

Datos=(name,direc,tfno)
print("Los datos personales son: ", Datos[0], ",", Datos[1], ",", Datos[2])

print("ejercicio 3")

num1=float(input("n1 "))
num2=int(input("n2 "))
num3=int(input("n3 "))

print((num1+num2+num3)/3)
