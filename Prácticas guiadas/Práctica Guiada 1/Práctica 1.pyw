from tkinter import *
from tkinter import Text
from tkinter import messagebox
import sqlite3

root=Tk()
frame=Frame(root)
frame.pack()
#-----------Funciones-------------
def conectar():

	conexion=sqlite3.connect("Usuarios")

	cursor=conexion.cursor()
	try:
		cursor.execute('''
		CREATE TABLE DATOS_USUARIOS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT, 
		NOMBRE_USUARIO VARCHAR(50),	
		PASSWORD VARCHAR(30),
		APELLIDO VARCHAR(50),
		DIRECCION VARCHAR(50),
		COMENTARIOS VARCHAR(100))
		''')
		messagebox.showinfo("BBDD","Base de datos creada con éxito")
	except:
		messagebox.showwarning("BBDD","La base de datos ya existe")
	conexion.close()

def salir():

	root.destroy()

def borrar_campos():

	ID.set("")
	nombre.set("")
	password.set("")
	apellido.set("")
	direccion.set("")
	comentarios.set("")

def create():

	usuario=(nombre.get(), password.get(), apellido.get(),
		direccion.get(), comentarios.get())
	
	conexion=sqlite3.connect("Usuarios")
	cursor=conexion.cursor()

	cursor.executemany("INSERT INTO DATOS_USUARIOS VALUES (NULL,?,?,?,?,?)", [usuario])
	conexion.commit()

	ID.set("")
	nombre.set("")
	password.set("")
	apellido.set("")
	direccion.set("")
	comentarios.set("")

	conexion.close()

def read():

	conexion=sqlite3.connect("Usuarios")
	cursor=conexion.cursor()
	
	leerID=int(ID.get())

	cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID={leerID}".\
        format(leerID=leerID))
	leerTupla=cursor.fetchall()

	for i in leerTupla:
		ID.set(i[0])
		nombre.set(i[1])
		password.set(i[2])
		apellido.set(i[3])
		direccion.set(i[4])
		comentarios.set(i[5])

	conexion.commit()

	conexion.close()

def update():

	conexion=sqlite3.connect("Usuarios")
	cursor=conexion.cursor()

	ids=int(ID.get())
	nombres=nombre.get()
	contra=password.get()
	apellidos=apellido.get()
	dire=direccion.get()
	coment=comentarios.get()

	cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?", (nombres,contra,apellidos,dire,coment,ids))

	conexion.commit()

	conexion.close()

def delete():

	conexion=sqlite3.connect("Usuarios")
	cursor=conexion.cursor()

	ids=int(ID.get())

	cursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID={id}".\
		format(id=ids))

	conexion.commit()

	ID.set("")
	nombre.set("")
	password.set("")
	apellido.set("")
	direccion.set("")
	comentarios.set("")

	conexion.close()

#-----------Menú desplegable------------
barraMenu=Menu(root)
root.config(menu=barraMenu)

BBDD=Menu(barraMenu,tearoff=0)
BBDD.add_command(label="Conectar",command=lambda:conectar())
BBDD.add_command(label="Salir", command=lambda:salir())
barraMenu.add_cascade(label="BBDD", menu=BBDD)

borrar=Menu(barraMenu, tearoff=0)
borrar.add_command(label="Borrar campos",command=lambda:borrar_campos())
barraMenu.add_cascade(label="Borrar", menu=borrar)

CRUD=Menu(barraMenu,tearoff=0)
CRUD.add_command(label="Create",command=lambda:create())
CRUD.add_command(label="Read",command=lambda:read())
CRUD.add_command(label="Update",command=lambda:update())
CRUD.add_command(label="Delete",command=lambda:delete())
barraMenu.add_cascade(label="CRUD", menu=CRUD)

#------------Esqueleto del programa------------
ID=StringVar()
cuadroID=Entry(frame, textvariable=ID)
cuadroID.config(fg="blue", justify="right")
IDLabel=Label(frame, text="ID:")

IDLabel.grid(row=1,column=1)
cuadroID.grid(row=1,column=2,padx=30,pady=10,columnspan=3)

nombre=StringVar()
cuadroNombre=Entry(frame,textvariable=nombre)
nombreLabel=Label(frame, text="Nombre:")

nombreLabel.grid(row=2,column=1)
cuadroNombre.grid(row=2,column=2,padx=30,pady=10,columnspan=3)

password=StringVar()
cuadroPassword=Entry(frame, textvariable=password)
cuadroPassword.config(fg="green", justify="center", show="@")
passwordLabel=Label(frame, text="Contraseña:")

passwordLabel.grid(row=3,column=1)
cuadroPassword.grid(row=3,column=2,padx=30,pady=10,columnspan=3)

apellido=StringVar()
cuadroApellido=Entry(frame, textvariable=apellido)
apellidoLabel=Label(frame, text="Apellidos:")

apellidoLabel.grid(row=4,column=1)
cuadroApellido.grid(row=4,column=2,padx=30,pady=10,columnspan=3)

direccion=StringVar()
cuadroDireccion=Entry(frame, textvariable=direccion)
direccionLabel=Label(frame, text="Dirección:")

direccionLabel.grid(row=5,column=1)
cuadroDireccion.grid(row=5,column=2,padx=30,pady=10,columnspan=3)

comentarios=StringVar()
cuadroComentarios=Entry(frame, textvariable=comentarios)
comentariosLabel=Label(frame, text="Comentarios:")

comentariosLabel.grid(row=6,column=1)
cuadroComentarios.grid(row=6,column=2,padx=30,pady=10,columnspan=3)

#botones
buttonCreate=Button(frame, text="Create", command=lambda:create())
buttonRead=Button(frame, text="Read", command=lambda:read())
buttonUpdate=Button(frame, text="Update", command=lambda:update())
buttonDelete=Button(frame, text="Delete",command=lambda:delete())

buttonCreate.grid(row=7,column=1)
buttonRead.grid(row=7,column=2)
buttonUpdate.grid(row=7,column=3)
buttonDelete.grid(row=7,column=4)


root.mainloop()