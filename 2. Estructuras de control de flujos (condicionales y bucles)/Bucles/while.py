#importamos las funciones matemáticas de Python
import math
i=1
while i<=10:
	print("Ejecución "+str(i))
	i=i+1
print("Terminó la ejecución")

edad=int(input("Introduce tu edad: "))

while edad<18 or edad>120:
	print("Edad incorrecta")
	edad=int(input("Introduce tu edad: "))

print("Acceso concedido")

print("Programa de cálculo de raíz cuadrada")
n=int(input("Introduce un número: "))

intentos=0

while n<=0:
	print("Los números negativos y 0 no tienen raíz")

	if intentos==5:
		print("Consumiste la prueba gratuita, +5.99€ al mes por usar el programa")
	#Salir del bucle
		break;

	n=int(input("Introduce un número: "))
	if n<=0:
		intentos=intentos+1
		
if intentos<5:
	raiz=math.sqrt(n)	
	print("La raíz cuadrada de " + str(n) + " es " + str(raiz))