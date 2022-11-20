from tkinter import *

root=Tk()
root.resizable(1,1)
root.iconbitmap("google_classroom.ico")
#creamos un frame que está en la raíz
Frame1=Frame(root, width=500, height=500)
Frame2=Frame(root, width=500, height=900)
Frame1.pack()
Frame2.pack()
#creamos un label
miLabel=Label(Frame1, text="Hola alumnos de python", fg="#0000FF",font=("Comic Sans MS",18))
#lo posicionamos
miLabel.place(x=0,y=0)
imagen=PhotoImage(file="imagen.gif")
miLabel2=Label(Frame1, image=imagen)
miLabel2.place(x=0,y=100)
#creamos una entrada
cuadroTexto=Entry(Frame2,bd=10,relief="groove")
nombreLabel=Label(Frame2, text="Nombre:",bd=10,relief="groove")
cuadroTexto.config(fg="blue", justify="right")

cuadroApellidos=Entry(Frame2,bd=10,relief="groove")
apellidosLabel=Label(Frame2, text="Apellidos:",bd=10,relief="groove")
cuadroApellidos.config(fg="red", justify="center")

cuadroDireccion=Entry(Frame2,bd=10,relief="groove")
direccionLabel=Label(Frame2, text="Dirección:",bd=10,relief="groove")
cuadroDireccion.config(fg="green", justify="left")

cuadroPass=Entry(Frame2,bd=10,relief="groove")
passLabel=Label(Frame2, text="Contraseña:",bd=10,relief="groove")
cuadroPass.config(fg="yellow", justify="center", show="@")

#manera 1
#nombreLabel.place(x=350,y=300)
#cuadroTexto.place(x=400,y=300)

#manera 2, grid,  (funciona como una tabla)
nombreLabel.grid(row=0, column=0, sticky="we",padx=10,pady=10)#sticky=alineacion con los puntos cardinales
cuadroTexto.grid(row=0, column=1, sticky="we",padx=10,pady=10)

apellidosLabel.grid(row=1, column=0, sticky="we",padx=10,pady=10)#padx, pady=márgenes en los ejes
cuadroApellidos.grid(row=1, column=1, sticky="we",padx=10,pady=10)

direccionLabel.grid(row=2, column=0, sticky="we",padx=10,pady=10)
cuadroDireccion.grid(row=2, column=1, sticky="we",padx=10,pady=10)

passLabel.grid(row=3, column=0, sticky="we",padx=10,pady=10)
cuadroPass.grid(row=3, column=1, sticky="we",padx=10,pady=10)

root.mainloop()

