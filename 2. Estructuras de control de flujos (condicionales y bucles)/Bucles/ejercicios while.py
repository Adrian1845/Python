print("ejercicio 1")

i=1
n2=0
while i==1:
	n1=int(input("Introduce un número: "))
	if n1>=n2:
		n1=int(input("Introduce un número: "))
		n2=n1

	if n2>n1:
		break;
print("Saliste del programa")

print("ejercicio 2")

nn1=int(input("Introduce un número positivo: "))
suma=0
while nn1>0:
	suma=suma+nn1
	nn1=int(input("Introduce un número positivo: "))
	if nn1<0:
		break;
print("La suma de los números que has introducido es: "+str(suma))