#!/usr/local/bin/python
# coding: latin-1
#evitar error UTF-8
def divide():
	try:
		op1=float(input("Introduce el primer n�mero: "))
		op2=float(input("Introduce el segundo n�mero: "))

		print("La divisi�n es: " +str(op1/op2))
	except: #excepci�n general
		print("Ha ocurrido un error")
	finally: #se ejecuta siempre, ocurra o no un error
		print("C�lculo finalizado.")

divide()