# Merge-Sort


def merge(listaA, listaB):
    lista = []
    i = 0
    j = 0

    while i < len(listaA) and j < len(listaB):
        if listaA[i] < listaB[j]:
            lista.append(listaA[i])
            i += 1
        else:
            lista.append(listaB[j])
            j += 1

    while i < len(listaA):
        lista.append(listaA[i])
        i += 1

    while j < len(listaB):
        lista.append(listaB[j])
        j += 1

    return lista


def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    listaA = mergeSort(lista[:meio])
    listaB = mergeSort(lista[meio:])
    return merge(listaA, listaB)


listaA = [1, 18, 33, 42]
listaB = [2, 13, 16, 46]
lista = merge(listaA, listaB)

print(lista)

lista = [18, 1, 33, 42, 16, 46, 2, 13]
lista = mergeSort(lista)

print(lista)

import random

# Quick-Sort
def partition(lista, esq, dir):
    r = random.randint(esq, dir)
    aux = lista[r]
    lista[r] = lista[esq]
    lista[esq] = aux
    j = esq
    pivot = lista[esq]
    for k in range(esq + 1, dir + 1):
        if lista[k] < pivot:
            j += 1
            aux = lista[k]
            lista[k] = lista[j]
            lista[j] = aux
    lista[esq] = lista[j]
    lista[j] = pivot
    return j


def quickSort(lista, esq, dir):
    if esq < dir:
        p = partition(lista, esq, dir)
        quickSort(lista, esq, p - 1)
        quickSort(lista, p + 1, dir)


lista = [18, 1, 33, 42, 53, 62, 13]
quickSort(lista, 0, len(lista)-1)
print(lista)