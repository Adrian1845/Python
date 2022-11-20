#!/usr/local/bin/python
# coding: latin-1
#evitar error UTF-8
def divide():
	try:
		op1=float(input("Introduce el primer número: "))
		op2=float(input("Introduce el segundo número: "))

		print("La división es: " +str(op1/op2))
	except: #excepción general
		print("Ha ocurrido un error")
	finally: #se ejecuta siempre, ocurra o no un error
		print("Cálculo finalizado.")

divide()