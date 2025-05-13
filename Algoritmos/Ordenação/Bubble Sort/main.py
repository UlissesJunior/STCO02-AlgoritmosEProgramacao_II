def bubble_sort(lista):
  k = len(lista) - 1
  for i in range(k, 0, -1):
    trocou = False
    for j in range(0, i, 1):
      if lista[j] > lista[j+1]:
        aux = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = aux
        trocou = True
    if trocou == False:
      return