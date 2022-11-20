import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintáxis sencilla"

textoBuscar="aprender"
textoBuscar2="Python"
#search(texto a buscar, donde buscarlo)
if re.search(textoBuscar, cadena) != None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")

textoEncontrado=re.search(textoBuscar, cadena)

#caracter dodne empieza (se empieza de 0 y los espacios cuentan) y donde termina
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

#ver cuantas veces está una palabra
print(len(re.findall(textoBuscar2,cadena)))
