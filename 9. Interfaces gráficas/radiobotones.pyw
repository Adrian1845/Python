#los radios botones son botones de una sola opción
from tkinter import *

root=Tk()

#la variable es un número
varOpcion=IntVar()

def imprimir():
	#print(varOpcion.get())

	if varOpcion.get()==1:
		etiqueta.config(text="Eres hombre")
	elif varOpcion.get()==2:
		etiqueta.config(text="Eres mujer")
	else:
		etiqueta.config(text="No eres normal")
Label(root, text="Género:").pack()
Radiobutton(root, text="Masculino",variable=varOpcion, value=1,command=(imprimir)).pack()
Radiobutton(root, text="Femenino",variable=varOpcion, value=2,command=(imprimir)).pack()
Radiobutton(root, text="No binario",variable=varOpcion, value=3,command=(imprimir)).pack()


etiqueta=Label(root)
etiqueta.pack()

root.mainloop()