from tkinter import *

root=Tk()
root.iconbitmap("calculadora.ico")
root.title("Calculadora")
Frame1=Frame(root)
Frame1.config(bg="black")
Frame1.pack()

#pantalla donde salen los números cuando los pulsamos

numeroPantalla=StringVar()

screen=Entry(Frame1, textvariable=numeroPantalla)
screen.grid(row=1, column=1, columnspan=4)
screen.config(bg="black", fg="#03f943", justify="right", highlightbackground="black",bd=10,relief="groove")

#pulsar las teclas
numero=""
def numeroPulsado(num):

	numeroPantalla.set(numeroPantalla.get()+num)

def operacion(num):

		numero=int(numeroPantalla.get())
		numeroPantalla.set("")


def igual():
		numero=operacion(numero)
		numeroPantalla.set(numero, int(numeroPantalla.get()))

#fila de botones, 7,8,9,x
button7=Button(Frame1,command=lambda:numeroPulsado("7"), text=7, width=5, bg="#21a8bd")
button7.grid(row=2,column=1)
button8=Button(Frame1,command=lambda:numeroPulsado("8"), text=8, width=5, bg="#21a8bd")
button8.grid(row=2,column=2)
button9=Button(Frame1,command=lambda:numeroPulsado("9"), text=9, width=5, bg="#21a8bd")
button9.grid(row=2,column=3)
buttonDividir=Button(Frame1,command=lambda:operacion("/"), text="/", width=5, bg="#9d0d8e")
buttonDividir.grid(row=2,column=4)

#fila de botones, 4,5,6,x
button4=Button(Frame1, command=lambda:numeroPulsado("4"), text=4, width=5, bg="#21a8bd")
button4.grid(row=3,column=1)
button5=Button(Frame1,command=lambda:numeroPulsado("5"), text=5, width=5, bg="#21a8bd")
button5.grid(row=3,column=2)
button6=Button(Frame1,command=lambda:numeroPulsado("6"), text=6, width=5, bg="#21a8bd")
button6.grid(row=3,column=3)
buttonMultiplicar=Button(Frame1,command=lambda:operacion("-"), text="X", width=5, bg="#e8b010")
buttonMultiplicar.grid(row=3,column=4)

#fila de botones, 1,2,3,-
button1=Button(Frame1,command=lambda:numeroPulsado("1"), text=1, width=5, bg="#21a8bd")
button1.grid(row=4,column=1)
button2=Button(Frame1,command=lambda:numeroPulsado("2"), text=2, width=5, bg="#21a8bd")
button2.grid(row=4,column=2)
button3=Button(Frame1,command=lambda:numeroPulsado("3"), text=3, width=5, bg="#21a8bd")
button3.grid(row=4,column=3)
buttonRestar=Button(Frame1,command=lambda:operacion("-"), text="_", width=5,bg="#cc1717")
buttonRestar.grid(row=4,column=4)

#fila de botones, , 0 ,+, =
buttonDecimal=Button(Frame1,command=lambda:numeroPulsado(","), text=",", width=5, bg="#505050")
buttonDecimal.grid(row=5,column=1)
button0=Button(Frame1,command=lambda:numeroPulsado("0"), text=0, width=5, bg="#21a8bd")
button0.grid(row=5,column=2)
buttonSumar=Button(Frame1,command=lambda:operacion("+"), text="+", width=5, bg="#41d810")
buttonSumar.grid(row=5,column=3)
buttonIgual=Button(Frame1, command=lambda:igual(), text="=", width=5,bg="#167DD2")
buttonIgual.grid(row=5,column=4)
root.mainloop()