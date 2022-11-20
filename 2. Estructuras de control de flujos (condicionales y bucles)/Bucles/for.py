#estructura: palabra reservada for, variable, palabra reservada in, elemento a recorrer
for i in [1,2,3]:
	print("hola")
for i in ["primavera","verano","otoño","invierno"]:
	print(i)

#recorrer strings
email=False

email1=str(input("Introduce tu correo: "))

for i in email1:
	if (i=="@" and i=="."):
	 email=True
#se puede acortar poniendo if email:
if email==True:
	print("Email correcto")
else:
	print("Email incorrecto")

#ejemplo más complejo
contador=0

email=str(input("Introduce tu correo: "))

for i in email:
	if (i=="@" or i=="."):
	 contador+=1

if contador==2:
	print("Email correcto")
else:
	print("Email incorrecto")

#range
for i in range(5):
	print(i, end="")

#funcion tipo f(concatenación) + variable
for i in range(0,10,2): #sintáxis: (número que empieza, número que acaba, de cuanto en cuanto)
	print(f"valor de la variable i:{i}")

#length
email=False

email1=str(input("Introduce tu correo: "))

for i in range(len(email1)):
	if email1[i]=="@":
	 email=True
if email:
	print("Email correcto")
else:
	print("Email incorrecto")





