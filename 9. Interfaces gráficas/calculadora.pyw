from tkinter import *
import cmath

root=Tk()
root.iconbitmap("calculadora.ico")
root.title("Calculadora")
Frame1=Frame(root)
Frame1.config(bg="black")
Frame1.pack()

#pantalla donde salen los números cuando los pulsamos

numeroPantalla=StringVar()

screen=Entry(Frame1, textvariable=numeroPantalla)
screen.grid(row=1, column=1, columnspan=3)#tamaño de la pantalla
screen.config(bg="black", fg="#03f943", justify="right", highlightbackground="black",bd=10,relief="groove")
#boton para los decimales
buttondecimal=Button(Frame1,command=lambda:decimales(), text="Decimal", width=5, bg="#f08739")
buttondecimal.grid(row=1,column=4)

#variables globales
operacion=""
resultado=0
reset_pantalla=False
num1=0
decimal=False
contador_decimal=0

def decimales():
	global decimal
	global contador_decimal
	if contador_decimal==0:
		decimal=True
		contador_decimal=1
	else:
		decimal=False
		contador_decimal=0
#pulsar la tecla
def numeroPulsado(num):
	global reset_pantalla

	if reset_pantalla!=False:
	
		numeroPantalla.set(num)
	
		reset_pantalla=False
	
	else:
	
		numeroPantalla.set(numeroPantalla.get()+num)

def suma(num):

		global operacion

		global resultado
		
		global reset_pantalla

		global decimal

		if decimal!=True:
			resultado+=int(num)
		else:
			resultado+=float(num)
		operacion="suma"
		
		reset_pantalla=True
		
		numeroPantalla.set(resultado)

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	global decimal

	if decimal!=True:

		if contador_resta==0:

			num1=int(num)

			resultado=num1

		else:

			if contador_resta==1:

				resultado=num1-int(num)

			else:

				resultado=int(resultado)-int(num)	

			numeroPantalla.set(resultado)

			resultado=numeroPantalla.get()
	else:
		if contador_resta==0:

			num1=float(num)

			resultado=num1

		else:

			if contador_resta==1:

				resultado=num1-float(num)

			else:

				resultado=float(resultado)-float(num)	

			numeroPantalla.set(resultado)

			resultado=numeroPantalla.get()
	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True

contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla

	global decimal

	if decimal!=True:
	
		if contador_multi==0:

			num1=int(num)
			
			resultado=num1

		else:

			if contador_multi==1:

				resultado=num1*int(num)

			else:

				resultado=int(resultado)*int(num)	

			numeroPantalla.set(resultado)
			
			resultado=numeroPantalla.get()
	else:
			if contador_multi==0:

				num1=float(num)
			
				resultado=num1

			else:

				if contador_multi==1:

					resultado=num1*float(num)

				else:

					resultado=float(resultado)*float(num)	

			numeroPantalla.set(resultado)
			
			resultado=numeroPantalla.get()

	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True


def raiz(num):

	global operacion

	global resultado

	global num1

	global reset_pantalla

	global decimal

	if decimal!=True:

		num1=int(num)

	else:
		num1=float(num)

	resultado=cmath.sqrt(num1)

	numeroPantalla.set(resultado)

	reset_pantalla=True

	resultado=0

def expo(num):

	global operacion

	global resultado

	global num1

	global reset_pantalla

	global decimal

	if decimal!=True:

		num1=int(num)

	else:
		num1=float(num)

	resultado=num1

	numeroPantalla.set(resultado)

	resultado=numeroPantalla.get()

	operacion="expo"

	reset_pantalla=True

def porcentaje(num):

	global operacion

	global resultado

	global num1

	global reset_pantalla

	global decimal

	if decimal!=True:

		num1=int(num)

	else:

		num1=float(num)

	resultado=num1

	numeroPantalla.set(resultado)

	resultado=numeroPantalla.get()

	operacion="porcentaje"

	reset_pantalla=True

def igual(num):
	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi

	global decimal

	if decimal!=True:
		if operacion=="suma":

			numeroPantalla.set(resultado+int(numeroPantalla.get()))

			resultado=0

		elif operacion=="resta":

			numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

			resultado=0

			contador_resta=0

		elif operacion=="multiplicacion":

			numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

			resultado=0

			contador_multi=0

		elif operacion=="division":

			numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

			resultado=0

			contador_divi=0

		elif operacion=="expo":

			numeroPantalla.set(int(resultado)**int(numeroPantalla.get()))

			resultado=0

		elif operacion=="porcentaje":
			numeroPantalla.set(int(resultado)/100*int(numeroPantalla.get()))
	else:
		if operacion=="suma":

			numeroPantalla.set(resultado+float(numeroPantalla.get()))

			resultado=0

		elif operacion=="resta":

			numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

			resultado=0

			contador_resta=0

		elif operacion=="multiplicacion":

			numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

			resultado=0

			contador_multi=0

		elif operacion=="division":

			numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))

			resultado=0

			contador_divi=0

		elif operacion=="expo":

			numeroPantalla.set(float(resultado)**float(numeroPantalla.get()))

			resultado=0

		elif operacion=="porcentaje":
			numeroPantalla.set(float(resultado)/100*float(numeroPantalla.get()))

def CE():
	global operacion
	global resultado
	global decimal
	global reset_pantalla
	numeroPantalla.set("")
	resultado=0
	operacion=""
	reset_pantalla=True
	decimal=False

#------------------------------------------------------------fila de botones, 7,8,9,/------------------------------------------------------------
button7=Button(Frame1,command=lambda:numeroPulsado("7"), text=7, width=5, bg="#21a8bd")
button7.grid(row=2,column=1)

button8=Button(Frame1,command=lambda:numeroPulsado("8"), text=8, width=5, bg="#21a8bd")
button8.grid(row=2,column=2)

button9=Button(Frame1,command=lambda:numeroPulsado("9"), text=9, width=5, bg="#21a8bd")
button9.grid(row=2,column=3)

buttonDividir=Button(Frame1,command=lambda:divide(numeroPantalla.get()), text="/", width=5, bg="#9d0d8e")
buttonDividir.grid(row=2,column=4)

#------------------------------------------------------------fila de botones, 4,5,6,x------------------------------------------------------------
button4=Button(Frame1, command=lambda:numeroPulsado("4"), text=4, width=5, bg="#21a8bd")
button4.grid(row=3,column=1)

button5=Button(Frame1,command=lambda:numeroPulsado("5"), text=5, width=5, bg="#21a8bd")
button5.grid(row=3,column=2)

button6=Button(Frame1,command=lambda:numeroPulsado("6"), text=6, width=5, bg="#21a8bd")
button6.grid(row=3,column=3)

buttonMultiplicar=Button(Frame1,command=lambda:multiplica(numeroPantalla.get()), text="X", width=5, bg="#ffff03")
buttonMultiplicar.grid(row=3,column=4)

#------------------------------------------------------------fila de botones, 1,2,3,-  -----------------------------------------------------------
button1=Button(Frame1,command=lambda:numeroPulsado("1"), text=1, width=5, bg="#21a8bd")
button1.grid(row=4,column=1)

button2=Button(Frame1,command=lambda:numeroPulsado("2"), text=2, width=5, bg="#21a8bd")
button2.grid(row=4,column=2)

button3=Button(Frame1,command=lambda:numeroPulsado("3"), text=3, width=5, bg="#21a8bd")
button3.grid(row=4,column=3)

buttonRestar=Button(Frame1,command=lambda:resta(numeroPantalla.get()), text="_", width=5,bg="#cc1717")
buttonRestar.grid(row=4,column=4)

#------------------------------------------------------------fila de botones, , 0 ,+, =------------------------------------------------------------
buttonDecimal=Button(Frame1,command=lambda:numeroPulsado("."), text=",", width=5, bg="#505050")
buttonDecimal.grid(row=5,column=1)

button0=Button(Frame1,command=lambda:numeroPulsado("0"), text=0, width=5, bg="#21a8bd")
button0.grid(row=5,column=2)

buttonSumar=Button(Frame1,command=lambda:suma(numeroPantalla.get()), text="+", width=5, bg="#41d810")
buttonSumar.grid(row=5,column=3)

buttonIgual=Button(Frame1,command=lambda:igual(numeroPantalla.get()), text="=", width=5,bg="#167DD2")
buttonIgual.grid(row=5,column=4)

#------------------------------------------------------------fila de botones CE, √ , ^, %------------------------------------------------------------
buttonCE=Button(Frame1,command=lambda:CE(), text="CE", width=5, bg="#be2590")
buttonCE.grid(row=6,column=1)

buttonRoot=Button(Frame1, command=lambda:raiz(numeroPantalla.get()),text="√", width=5, bg="#5f15c8")
buttonRoot.grid(row=6,column=2)

buttonExpo=Button(Frame1,command=lambda:expo(numeroPantalla.get()), text="^", width=5, bg="#17dc91")
buttonExpo.grid(row=6,column=3)

buttonPercentaje=Button(Frame1,command=lambda:porcentaje(numeroPantalla.get()), text="%", width=5,bg="#8f9eb0")
buttonPercentaje.grid(row=6,column=4)

root.mainloop()