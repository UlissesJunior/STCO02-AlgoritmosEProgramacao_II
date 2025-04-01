lista = [5, 99, 13, 18, 1, 30]

# Bubble Sort
def bubbleSort(lista):
    k = len(lista) - 1
    for i in range(k, 0, -1):
        trocou = False
        for j in range(0, i, 1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocou = True
        if(trocou == False):
            return
        
def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i
        valor = lista[j]
        while j > 0 and lista[j-1] > valor:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = valor
        
def selectionSort(lista):
    for i in range (len(lista)):
        indiceMenor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indiceMenor]:
                indiceMenor = j
        aux = lista[i]
        lista[i] = lista[indiceMenor]
        lista[indiceMenor] = aux