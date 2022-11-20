import sqlite3

conexion=sqlite3.connect("UNIQUE, update y delete")

cursor=conexion.cursor()

#cursor.execute('''
	#CREATE TABLE PRODUCTOS (
	#ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	#NOMBRE_ARTÍCULO VARCHAR(50) UNIQUE, #UNIQUE = no se puede repetir valor	
	#PRECIO INTEGER,	
	#SECCION VARCHAR(20))
#''')

#productos=[
	#("PELOTA", 20, "JUGUETERÍA"),
	#("PANTALÓN", 15, "ROPA"),
	#("DESTORNILLADOR", 25, "HERRAMIENTAS"),
	#("JARRÓN", 45, "CERÁMICA"),	
	#("TAZA", 410, "CERÁMICA")	
#]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) #insertar en la tabla productos

#cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='CERÁMICA'") #READ
#cursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE ID=5") #UPDATE

cursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")

conexion.commit()

conexion.close()
