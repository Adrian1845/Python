import sqlite3
from tkinter import *

root=Tk()
root.title("BBDD")
root.geometry("500x500")

frame1=Frame(root)
frame1.config(bg="#505050", height=300, width=300)
frame1.pack()
def crear():
	nombre=str(input("¿Qué nombre deseas darle?"))
	conexion=sqlite3.connect(str(nombre))
	cursor=conexion.cursor()
	cursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	NOMBRE_ARTÍCULO VARCHAR(50),	
	PRECIO INTEGER,
	SECCION VARCHAR(20))
	''')

	conexion.close()
def ver():
	base_de_datos=str(input("¿Qué base de datos quieres ver?: "))
	producto=int(input("¿Qué producto quieres ver?: "))
	conexion=sqlite3.connect(str(base_de_datos))

	cursor=conexion.cursor()

	cursor.execute("SELECT * FROM PRODUCTOS")
	
	variosProductos=cursor.fetchall()
	print(variosProductos[producto])
	
	conexion.close()

def añadir():
	base_de_datos=str(input("¿A qué base de datos quieres añadir un producto?"))
	conexion=sqlite3.connect(str(base_de_datos))
	cursor=conexion.cursor()

	nombre_articulo=str(input("introduce el nombre del artículo: "))
	precio_articulo=int(input("introduce el precio del artículo: "))
	seccion_articulo=str(input("introduce la seccion del articulo: "))


	añadir_producto=(nombre_articulo,precio_articulo,seccion_articulo)
	

	cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", [añadir_producto])
	conexion.commit()
	conexion.close()

crear_base_de_datos=Button(frame1, text="crear base de datos", command=lambda:crear())
crear_base_de_datos.grid(row=1,column=1)
ver_base_de_datos=Button(frame1, text="ver base de datos", command=lambda:ver())
ver_base_de_datos.grid(row=1,column=2)
añadir_a_base_de_datos=Button(frame1, text="añadir a base de datos", command=lambda:añadir())
añadir_a_base_de_datos.grid(row=1,column=3)
root.mainloop()