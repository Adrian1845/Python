from tkinter import *
#importar ventana emergente
from tkinter import messagebox

root=Tk()

#ventana emergente
def about_us():
	messagebox.showinfo("About us","Maricón")#título de la ventana emergente, mensaje de la ventana emergente

def licencia():
	messagebox.showwarning("Licencia","No hay xd")#advertencia

def salir():
	valor=messagebox.askquestion("Salir","¿De verdad quieres salir?")#botones, si y no, devuelven yes or no

	if valor=="yes":
		root.destroy()#terminar con el programa

def guardar():
	valor=messagebox.askokcancel("Guardar","¿De verdad quieres guadar?")#botones, ok y cancelar, devuelven True or False

def cerrar():
	valor=messagebox.askretrycancel("Cerrar","No es posible cerrar, documento bloqueado")#boton, retry y cancel, devuelven True or False

	if valor==False:
		root.destroy()

#declaramos el menú y ponemos que menú es el de root
barraMenu=Menu(root)

root.config(menu=barraMenu, width=500, height=500)

#declaramos los apartados del menú
file=Menu(barraMenu,tearoff=0)#tearoff=quitar las lineas ---- 
#añadir submenús
file.add_command(label="Nuevo")
file.add_command(label="Guardar", command=guardar)
file.add_command(label="Guardar como")
file.add_separator()#añadir barra separadora
file.add_command(label="Cerrar", command=cerrar)
file.add_command(label="Salir", command=salir)

edit=Menu(barraMenu)
edit.add_command(label="Copiar")
edit.add_command(label="Cortar")
edit.add_command(label="Pegar")

selection=Menu(barraMenu,tearoff=0)
selection.add_command(label="Select all")
selection.add_command(label="Single selection")
selection.add_command(label="Invert selection")

find=Menu(barraMenu)
view=Menu(barraMenu)

helps=Menu(barraMenu)
helps.add_command(label="Acerca de...", command=about_us)
helps.add_command(label="Licencia", command=licencia)

#añadimos los elementos del menú y le damos el texto que queremos que aparezca
barraMenu.add_cascade(label="File", menu=file)
barraMenu.add_cascade(label="Edit", menu=edit)
barraMenu.add_cascade(label="Selection", menu=selection)
barraMenu.add_cascade(label="Find", menu=find)
barraMenu.add_cascade(label="View", menu=view)
barraMenu.add_cascade(label="Help", menu=helps)


root.mainloop()