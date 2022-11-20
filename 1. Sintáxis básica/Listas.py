#creación de lista
nombresEx=["Andrea","Yaiza","Mónica","Rocío"]

print(nombresEx[:])

#llamar un índice (se empieza por el 0)
print(nombresEx[2])

#índice negativo (empieza desde -1)
print(nombresEx[-4])

#rangos (segundo número no inclusive)
print(nombresEx[0:2])
print(nombresEx[1:3])

#excluir un rango
print(nombresEx[:4])
print(nombresEx[2:])

#agregar al final de la lista
nombresEx.append("Eva")
print(nombresEx[:])

#insetar en la lista
nombresEx.insert(0,"Claudia")
print(nombresEx[:])

#añadir elementos a la lista
nombresEx.extend(["ex1","ex2","ex3"])
print(nombresEx[:])

#devolver índices
print(nombresEx.index("Rocío"))

#comprobar si está el elemento en la lista
print("Noelia" in nombresEx)

#varios tipos de datos en la lista
nombresEx2=["Andrea",2,"Mónica",True]
print(nombresEx[1:])

#eliminar elementos
nombresEx2.remove(2)
print(nombresEx2[:])

#eliminar último elemento de una lista
nombresEx2.pop()
print(nombresEx2[:])

#juntar listas
nombresEx3=nombresEx+nombresEx2
print(nombresEx3[:])

#repetidor
nombresEx4=nombresEx2*3
print(nombresEx4[:])

#convertir lista en tupla
Lista=["yo","pivon"]
Tupla=tuple(Lista)
print(Tupla)