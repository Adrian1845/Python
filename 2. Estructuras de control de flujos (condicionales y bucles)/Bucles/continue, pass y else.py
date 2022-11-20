#continue
for letra in "Python":
	

	if letra=="h":
		continue#ignora el resto del bucle

	print("Viendo la letra: " +letra)

nombre="Adrián es muy guapo"

contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1 #contador++

print(contador)

#pass (para completarlo luego y que siga corriendo el programa)
while True:
	pass

class MiClase:
	pass

#else
email=input("Intreoduce tu email: ")

for i in email:
	if i=="@":
		arroba=True

		break;
else:
	arroba=False

print(arroba)