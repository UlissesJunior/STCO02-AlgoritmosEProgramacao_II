def selection_sort(lista):
  for i in range(len(lista)):
    indice_menor = i
    for j in range(i+1, len(lista)):
      if lista[j] < lista[indice_menor]:
        indice_menor = j
    aux = lista[i]
    lista[i] = lista[indice_menor]
    lista[indice_menor] = aux