'''def area_triangulo(base, altura):

	return (base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(6,9)

print(triangulo1)
print(triangulo2)'''

#las funciones lambda sirven para simplificar el código
area_triangulo= lambda base, altura: (base*altura)/2

print(area_triangulo(5,7))
print(area_triangulo(6,9))

cubo=lambda numero:pow(numero,3)

print(cubo(13))

valor=lambda comision: "¡{}!€".format(comision)

print(valor(15585))

