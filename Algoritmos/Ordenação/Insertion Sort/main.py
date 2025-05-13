def insertion_sort(lista):
  for i in range(1, len(lista)):
    j = i
    valor = lista[j]
    while j > 0 and lista[j-1] > valor:
      lista[j] = lista[j-1]
      j = j - 1
    lista[j] = valor