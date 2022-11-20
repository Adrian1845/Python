#declarar una función sin parámetros
def mensaje():
    print("Me gustan las tortugas")

#llamar a la función
mensaje()

#se pueden poner líneas de código entre las llamadas 
print("ejemplo")
mensaje()

#función con argumentos
def suma(n1, n2):
    print(n1+n2)

suma(2,3)

suma(5,7)

suma(123213,789123)

#función con return
def suma(n1, n2):
    resultado=n1+n2
    return resultado
    

print(suma(2,3))

print(suma(5,7))

suma(123213,789123)

#almacenar resultados de funciones
def suma(n1, n2):
    resultado=n1+n2
    return resultado

almacenResultado=suma(3,4)
print(almacenResultado)
