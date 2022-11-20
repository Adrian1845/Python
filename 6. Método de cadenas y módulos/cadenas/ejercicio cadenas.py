correo=input("Introduce tu correo electrónico: ")
contador=correo.count("@") #cuenta la cantidad de arrobas
print(correo.find("@"))
#si solo hay un arroba
#o si el arroba es igual a la longitud del correo -1 (no esté al final)
#o si el arroba es 0 (no esté al principio)
if(contador!=1 or correo.rfind("@")==(len(correo)-1) or correo.find("@")==0):
	print("Mail incorrecto")
else: 
	print("Mail correcto")
