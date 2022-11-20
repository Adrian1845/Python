#mayor o menor
salario_presidente=int(input("Introduce el salario del presidente: "))
print("salario presidente: "+str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("salario director: "+str(salario_director)) 

salario_jefe_area=int(input("Introduce el salario Jefe Área: "))
print("salario jefe área: "+str(salario_jefe_area)) 

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("salario administrativo: "+str(salario_administrativo)) 

if salario_presidente>salario_director>salario_jefe_area>salario_administrativo:
	print("No hay corrupción")
else:
	print("Se detectó un enchufado")