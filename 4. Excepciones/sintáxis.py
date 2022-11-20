#una excepción es un error inesperado que ocurre durante la ejecución
#ocurren cuando el código está bien redactado pero da error inesperado
#solo válido para código no vital
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:		
		return num1/num2 #da error al dividir por 0

	except ZeroDivisionError: #ponemos el nombre del error
		print("No se puede dividir entre 0")
		return "Operación erronea"
while True:
	try:
		op1=(int(input("Introduce el primer número: ")))

		op2=(int(input("Introduce el segundo número: ")))	
		break;
	except ValueError:
		print("Los valores introducidos no son números")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")

def evaluaEdad(edad):

	if edad<0:
		raise EdadNegativa("edad incorrecta")
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres mayor"
	elif edad<100:
		return "eres muy mayor"

print(evaluaEdad(-10))