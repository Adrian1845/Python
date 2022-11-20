#los checkbuttons son botones de varias opciones
from tkinter import *

root=Tk()

foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

etiqueta=Label(frame)
etiqueta.pack()

#asignamos que los botones son números
ciudad=IntVar()
montagna=IntVar()
playa=IntVar()

def opcionesViaje():

	global ciudad
	global montagna
	global playa

	opcionEscogida=""

	if(ciudad.get()==1):
		opcionEscogida+=" ciudad"
		
	if(montagna.get()==1):
		opcionEscogida+=" montaña"

	if(playa.get()==1):
		opcionEscogida+=" playa"

	textoFinal.config(text=opcionEscogida)

Label(frame, text="Elige tu destino").pack()
#creamos los botones
Checkbutton(frame, text="Ciudad", variable=ciudad, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña",variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Playa",variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()