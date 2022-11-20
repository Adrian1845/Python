#io es el método de almacenamiento externo
#se debe dar: creación, apertura, manipulación y cierre
from io import open
#dos argumentos:(nombre, forma de abrir el archivo)
#hay tres formas, lectura, escritura, append (añadir texto cuando ya hay)
#escritura
archivo_texto=open("ejemplo archivos externos.txt","w")

frase="Aprendiendo Python a las 19:26, \nUn 22 de agosto de 2020"

archivo_texto.write(frase)

archivo_texto.close()
print("-------")
#lectura
archivo_texto=open("ejemplo archivos externos.txt","r")

texto=archivo_texto.read()
#hacer que las lineas sean una lista
lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(texto)
print(lineas_texto)

#append
archivo_texto=open("ejemplo archivos externos.txt", "a")
archivo_texto.write("\nno me funciona la lista xd")
archivo_texto.close()
print("-------")
#desplazar el puntero
archivo_texto=open("ejemplo archivos externos.txt","r+") #lectura y escritura
archivo_texto.write("No funciona el puntero a la mitad")
archivo_texto.seek(12)
print(archivo_texto.read())
archivo_texto.close()
print("-------")
#colocar el puntero en la mitad
archivo_texto=open("ejemplo archivos externos.txt","r+")
archivo_texto.seek(len(archivo_texto.read()))
print(archivo_texto.read())

lista_texto=archivo_texto.readlines()

lista_texto[1]="Modificando la línea desde el exterior\n"
archivo_texto.close()