#sin generador
def generaPares(limite):

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2)

		num=num+1

	return miLista


print(generaPares(10))

#yield (construye un objeto, los va generando cada vez que llamo a la función)
def generaPares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvePares=generaPares(99)

print(next(devuelvePares))

print("Más código")

print(next(devuelvePares))

print("Más código")

print(next(devuelvePares))

#yield from
def devuelve_ciudades(*ciudades): #el * indica que se recibirán indeterminados elementos en forma de tupla
	for elemento in ciudades:
		#for i in elemento:
			#yield i
			yield from elemento



ciudades_devueltas=devuelve_ciudades("Madrid", "Toledo", "Barcelona", "Ávila", "Málaga")

print(next(ciudades_devueltas)) 
print(next(ciudades_devueltas)) 
