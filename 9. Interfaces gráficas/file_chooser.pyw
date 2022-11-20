from tkinter import *
#importamos la librería de abrir archivos
from tkinter import filedialog
from tkinter import colorchooser

root=Tk()
root.config(height=300,width=300)
def abreFichero():

	fichero=filedialog.askopenfilename(title="Abrir archivo", initialdir="E:", filetypes=(("Ficheros de Excel","*.xlsx")
		,("Ficheros de texto","*.txt"),("Todos los ficheros","*.*")))

	print(fichero)


def chooser():

	color=colorchooser.askcolor()
	fondo=color[1]
	root.config(bd=fondo)

Button (root, text="Abrir archivo", command=abreFichero).pack()
Button (root, text="Seleccionar color", command=chooser).pack()

root.mainloop()
