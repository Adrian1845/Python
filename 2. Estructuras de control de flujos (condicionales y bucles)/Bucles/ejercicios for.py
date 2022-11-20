print("ejercicio 1")

for i in range(1,100,2): print(i, end=" ")

print(" ")

print("ejercicio 2")

contrasena=str(input("Introduce tu contraseña: "))
contador=0
for i in range(len(contrasena)): 
	if contrasena[i]==" ":
		contador=1

if (len(contrasena)<8 or contador==1):
	print("contraseña incorrecta")
else:
	print("contraseña correcta")

print("ejercicio 3")

contadorArroba=0
contadorPunto=0

email=input("Introduce tu correo: ")

for i in email:
	if (i=="@"):
		contadorArroba=1

	if (i=="."):
		contadorPunto=contadorPunto+1


if contadorArroba==1 and contadorPunto!=0:
	print("Email correcto")
else:
	print("Email incorrecto")


