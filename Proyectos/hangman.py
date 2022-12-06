import random, sys
def get_nth_key(dictionary, n):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

dic = {
"perro":'''Mamífero carnívoro doméstico de la familia de los cánidos que se caracteriza por 
tener los sentidos del olfato y el oído muy finos, por su inteligencia y por su fidelidad al ser humano,
que lo ha domesticado desde tiempos prehistóricos; hay muchísimas razas, de características muy diversas.''',
"gatos":'''Mamífero felino de tamaño generalmente pequeño, cuerpo flexible, cabeza redonda, 
patas cortas, cola larga, pelo espeso y suave, largos bigotes y uñas retráctiles; es carnívoro y 
tiene gran agilidad, buen olfato, buen oído y excelente visión nocturna; existen muchas especies diferentes.''',
"huevo": '''Cuerpo redondo u ovalado, con una membrana o cáscara exterior, que ponen las hembras de 
algunos animales y que contiene en su interior el embrión de un nuevo ser y el alimento 
necesario para que crezca.''',
"linea":'''Señal o marca larga y estrecha que se hace o se forma sobre un cuerpo o superficie.'''
}
contador=0
lista = []
indice=random.randint(0,len(dic)-1)
palabra = get_nth_key(dic, indice)
#contador
while (contador<=3):
    win = True
    appears = False
    appearsLista = False
    #introducimos el char
    print("\nPista: ",dic[palabra])
    letra = input("\nIntroduce la letra: ")[0]
    #añadimos la letra a la lista
    lista.append(letra)
    #recorre la palabra mediante i
    for i in palabra:
        if i == letra:
            print(i,end="",flush=True)
            appears=True
        #si i no está
        elif i != letra:
            #recorre las letras de la lista de letras que ya hemnos introducido
            for x in lista:
                #si la letra de la lista es igual a la letra de la palabra
                if x == i:
                    #sacame la letra y cambio la variable de control
                     print(i,end="",flush=True)
                     appearsLista=True
            #si la variable de control es falsa, no hay ninguna letra en la lista que coincida con la letra a buscar
            if not appearsLista:
                print("_",end="",flush=True)
                win = False
            #una vez hemos sacado la letra o el hueco, ponemos la variable de control a falso para las siguientes comprobaciones
            appearsLista=False
    if not appears:
        win = False
        contador+=1
        print("\nLa letra no está, tú numero de fallos es: ",contador)
    print("\nHas usado las siguientes letras: ",lista)

    if win:
        print("Enhorabuena fiera, un saludo para la mama")
        sys.exit()
print("La palabra era: ",palabra)
print("Más suerte la próxima vez")

