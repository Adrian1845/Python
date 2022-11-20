#acceder a un elemento del diccionario
#estructura clave:elemento
diccionario={"Alemania":"Berlín","Francia":"París"
,"Inglaterra":"Londres","España":"Madrid",16:"Rocío","Andrea":27}
print(diccionario["España"])

#agregar un elemento
diccionario["Italia"]="Lisboa"#erroneo para practicar
print(diccionario["Italia"])

#cambiar una clave
diccionario["Italia"]="Roma"
print(diccionario["Italia"])

#eliminar un elemento
del diccionario["Inglaterra"]
print(diccionario)

#tupla a diccionario
tupla=["España", "Francia", "Alemania"]
diccionario={tupla[0]:"Madrid",tupla[1]:"París",tupla[2]:"Berlín"}
print(diccionario)
print(diccionario[tupla[1]])

#varios elementos para una clave
diccionario={"España":{"Franco":[1936,1939]}#tupla dentro de diccionario
,"Francia":"París","Alemania":"Berlín"}
print(diccionario)
print(diccionario["España"])

#sacar solo las claves, valores y la longitud
print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))


