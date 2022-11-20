import sqlite3

conexion=sqlite3.connect("Campo clave")

cursor=conexion.cursor()

	#cursor.execute('''
		#CREATE TABLE PRODUCTOS (
		#CÓDIGO_ARTÍCULO VARCHAR(4) PRIMARY KEY, #Campo clave = PRIMARY KEY
		#NOMBRE_ARTÍCULO VARCHAR(50),	#VARCHAR = caracteres máximos del campo
		#PRECIO INTEGER,	#INTEGER =el dato es un número
		#SECCION VARCHAR(20))
	#''')

	#productos=[
		#("AR01", "PELOTA", 20, "JUGUETERÍA"),
		#("AR02", "PANTALÓN", 15, "ROPA"),
		#("AR03", "DESTORNILLADOR", 25, "HERRAMIENTAS"),
		#("AR04", "JARRÓN", 45, "CERÁMICA")	
	#]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos) #insertar en la tabla productos
#automatizar el campo clave
cursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT, #Campo clave = PRIMARY KEY, AUTOINCREMENT=incrementar automáticamente
	NOMBRE_ARTÍCULO VARCHAR(50),	#VARCHAR = caracteres máximos del campo
	PRECIO INTEGER,	#INTEGER =el dato es un número
	SECCION VARCHAR(20))
''')

productos=[
	("PELOTA", 20, "JUGUETERÍA"),
	("PANTALÓN", 15, "ROPA"),
	("DESTORNILLADOR", 25, "HERRAMIENTAS"),
	("JARRÓN", 45, "CERÁMICA")	
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) #insertar en la tabla productos

conexion.commit()

conexion.close()