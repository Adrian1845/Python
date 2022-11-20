#extension pyw para que se ejecute sin la consola detrás
#importamos la libreria tkinter
from tkinter import *
#creamos la raíz
raiz=Tk()
#título de la interfaz
raiz.title("Ventana")

#bloquear la redimensionar
raiz.resizable(1,1)#ancho y alto (boolean)

#cambiar icono
raiz.iconbitmap("google_classroom.ico")

#crear ventana con diferente tamaño
raiz.geometry("1050x1050")

#cambiar el color de fondo
raiz.config(bg="grey",bd=10,relief="groove",cursor="hand2")

#https://docs.python.org/3.4/library/tkinter.html#packer-options
#crear un frame
miFrame=Frame()

#lo empaquetamos dentro de la raíz
miFrame.pack(side="bottom",anchor="w")#se quede anclado abajo e izquierda
#miFrame.pack(fill="y", expand="True") #para que se expanda en el eje "y"	

#todo el config del frame vale para la raiz
#cambiar el color de fondo y darle tamaño, cambiar el grosor del borde y ponerlo especial
miFrame.config(bg="black",width="250",height=("250"),bd=35,relief="sunken")

#cambiar el cursor
miFrame.config(cursor="pirate")

#creamos un bucle infinito para que se pueda ejecutar
#siempre debe estar en el último lugar
raiz.mainloop()

