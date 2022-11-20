from tkinter import *

root=Tk()
root.config(bg="grey")
Frame1=Frame(root, bg="grey")
Frame1.pack()

minombre=StringVar()

cuadroTexto=Entry(Frame1,bd=10,relief="groove",textvariable=minombre)
nombreLabel=Label(Frame1, text="Nombre:",bd=10,relief="groove")
cuadroTexto.config(fg="blue", justify="right")

cuadroApellidos=Entry(Frame1,bd=10,relief="groove")
apellidosLabel=Label(Frame1, text="Apellidos:",bd=10,relief="groove")
cuadroApellidos.config(fg="red", justify="center")

cuadroDireccion=Entry(Frame1,bd=10,relief="groove")
direccionLabel=Label(Frame1, text="Dirección:",bd=10,relief="groove")
cuadroDireccion.config(fg="green", justify="left")

cuadroPass=Entry(Frame1,bd=10,relief="groove")
passLabel=Label(Frame1, text="Contraseña:",bd=10,relief="groove")
cuadroPass.config(fg="yellow", justify="center", show="@")

#crear un cuadro de comentarios
comentarioLabel=Label(Frame1, text="Comentarios:",bd=10,relief="sunken")
textoComentario=Text(Frame1, bd=11,relief="sunken",width=20,height=10)

#crear un scrollbar
scrollVert=Scrollbar(Frame1, command=textoComentario.yview)#poner la barra enganchada al eje y del comentario
scrollHorz=Scrollbar(Frame1, orient='horizontal', command=textoComentario.xview,)#poner la barra enganchada al eje x del comentario

#poner las scrollbars para que marquen en que parte estamos
textoComentario.config(yscrollcommand=scrollVert.set)
textoComentario.config(yscrollcommand=scrollHorz.set)

#crear un botón

def codigoBoton():
	
	minombre.set("Adrián")#establecer información de una variable

botonEnvio=Button(Frame1, text="Enviar", command=codigoBoton)

nombreLabel.grid(row=0, column=0, sticky="we",padx=10,pady=10)#sticky=alineacion con los puntos cardinales
cuadroTexto.grid(row=0, column=1, sticky="we",padx=10,pady=10)

apellidosLabel.grid(row=1, column=0, sticky="we",padx=10,pady=10)#padx, pady=márgenes en los ejes
cuadroApellidos.grid(row=1, column=1, sticky="we",padx=10,pady=10)

direccionLabel.grid(row=2, column=0, sticky="we",padx=10,pady=10)
cuadroDireccion.grid(row=2, column=1, sticky="we",padx=10,pady=10)

passLabel.grid(row=3, column=0, sticky="we",padx=10,pady=10)
cuadroPass.grid(row=3, column=1, sticky="we",padx=10,pady=10)

comentarioLabel.grid(row=4, column=0, sticky="we",padx=10,pady=10)
textoComentario.grid(row=4, column=1, sticky="we",padx=10,pady=10)

scrollVert.grid(row=4, column=2, sticky="nsew")
scrollHorz.grid(row=5, column=1, sticky="nsew")
botonEnvio.grid(row=6, column=0)
root.mainloop()

