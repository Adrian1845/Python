import random, sys
palabra = ["perro","gatos","huevo","linea","mario","jorge"]
contador=0
lista = []
indice=random.randint(0,len(palabra)-1)

#contador
while (contador<=3):
    win = True
    appears=False
    appearsLista=False
    #introducimos el char
    letra = input("\nIntroduce la letra: ")[0]
    #añadimos la letra a la lista
    lista.append(letra)
    #recorre la palabra mediante i
    for i in palabra[indice]:
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
            if appearsLista==False:
                print("_",end="",flush=True)
                win = False
            #una vez hemos sacado la letra o el hueco, ponemos la variable de control a falso para las siguientes comprobaciones
            appearsLista=False
    if appears==False:
        win = False
        contador+=1
        print("\nLa letra no está, tú numero de fallos es: ",contador)
    print("\nHas usado las siguientes letras: ",lista)

    if win == True:
        print("Enhorabuena fiera, un saludo para la mama")
        sys.exit()
print("La palabra era: ",palabra[indice])
print("Más suerte la próxima vez")