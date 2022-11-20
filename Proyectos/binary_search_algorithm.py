#binary search algorithm 

#In a nutshell, this search algorithm takes advantage of a 
#collection of elements that is already sorted by ignoring half of the elements after just one comparison. 
import random

def main(list, number):
    #declaro las variables inicio, el medio, fin (tamaño de la lista) y los pasos
    start=0
    middle=0
    end=len(list)
    steps=0
    #ordeno la lista para cuadrar el número medio
    list.sort()

    print("Programa binary search") 
    while(start<=end):

        print("")
        #cuento los pasos y muestro la lista con los indices del inicio al fin +1
        print("Pasos: ",steps," Número a buscar: ",number," ", str(list[start:end+1]), )
        
        steps+=1
        #declaramos el medio como la suma entre el inicio y el fin entre dos, al principio sería equivalente a fin / 2
        middle = (start+end) // 2

        if number == list[middle]:
            return number

        elif number < list[middle]:
            #si el numero es menor al medio, el fin se convierte en el medio -1
            end = middle-1
        else:
            #si el numero es mayor al medio, el inicio se convierte en el medio +1
            start = middle+1

#creo una lista aleatoria y la relleno de números (int) del 0 al 100
randomList = []

for i in range(0,50):
    n=random.randint(0,100)
    randomList.append(n)
#asigno el numero a un índice aleatorio de la lista, así el número está sí o sí en la lista
number = randomList[random.randint(0,50)]

print(main(randomList,number))