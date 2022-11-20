#manipulación de strings
#upper y lower
nombreUsuario=input("Introduce tu nombre: ")
print("Tu nombre es: ", nombreUsuario.upper())
print("Tu nombre es: ",nombreUsuario.lower())
#capitalize (primera letra en mayúscula)
print("Tu nombre es: ",nombreUsuario.capitalize())
#isdigit (devuelve True or False si es un dígito)
edad=input("Introduce la edad: ")
while (edad.isdigit()==False):
	edad=input("Introduce la edad: ")
if (int(edad)<18):
	print("No puedes pasar")
else:
	print("Puedes pasar")
