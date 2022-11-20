#Una Tupla es una lista que no se puede modificar
#se diferencia en que una tupla va entre paréntesis y
#una lista entre corchetes
nombreTupla=("elem1","elem2","elem3","elem2")
#convertir tupla a lista
nombreLista=list(nombreTupla)
print(nombreTupla)

#buscar elementos en tupla
print("elem1" in nombreTupla)

#cantidad de veces que está un elemento
print(nombreTupla.count("elem2"))

#longitud de la tupla
print(len(nombreTupla))

#tupla unitaria
tuplaUnitaria=("elem1",)
print(len(tuplaUnitaria))

#tupla sin paréntesis (empaquetado de tupla)
empTupla="elem1","elem2","elem3","elem2"
print(empTupla)

#desempaquetado de tuplas
dempTupla=("Dominadas",3,12,"90s")
ejercicio, series, reps, descanso=dempTupla
print(ejercicio)
print(series)
print(reps)
print(descanso)
nombresEx=["Andrea","Yaiza","Mónica","Rocío"]
