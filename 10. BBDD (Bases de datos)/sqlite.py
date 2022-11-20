#importamos la base de datos
import sqlite3

#creamos la conexión a la base de datos (crear la base de datos)
conexion=sqlite3.connect("Primera BDD")

#creamos el cursor
cursor=conexion.cursor()

#creamos la tabla (curso sqlite o MySQL). Esta linea solo se debe ejecutar una vez.
#cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTÍCULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#insertar productos
#cursor.execute("INSERT INTO PRODUCTOS VALUES('balón', 15, 'deportes')")

#podemos insertar varias tuplas a la vez
#variosProductos=[
	#("CAMISETA",10,"DEPORTES"),
	#("JARRÓN",90,"CERÁMICA"),
	#("CAMIÓN",20,"JEGUETERÍA")
#]
#introducir las tuplas, una ? por campo
#cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

#mostrar la información de la tabla
cursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=cursor.fetchall()
print(variosProductos[0])

for producto in variosProductos:
	print("Nombre Artículo: ",producto[0], " Precio: " ,producto[1]," Sección: ", producto[2])

#confirmar un cambio
conexion.commit()
#creamos la base de datos
conexion.close()