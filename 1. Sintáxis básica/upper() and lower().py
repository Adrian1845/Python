#lower(), ponerlo todo en minúsculas
print("Optativas 2020")
Optativas=["Informática gráfica, Pruebas de Software, Usabilidad y accesibilidad"]
print(Optativas)
asignaturas=input("Escribe la asignatura escogida: ")
asignatura=asignaturas.lower()
if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Has escogido: ", asignatura)
else:
	print("La asigantura escogida no está disponible")

#upper(), ponerlo todo en mayúsculas
print("Optativas 2020")
Optativas=["Informática gráfica, Pruebas de Software, Usabilidad y accesibilidad"]
print(Optativas)
asignaturas=input("Escribe la asignatura escogida: ")
asignatura=asignaturas.upper()
if asignatura in ("INFORMÁTICA GRÁFICA", "PRUEBAS SOFTWARE", "USABILIDAD Y ACCESIBILIDAD"):
	print("Has escogido: ", asignatura)
else:
	print("La asigantura escogida no está disponible")