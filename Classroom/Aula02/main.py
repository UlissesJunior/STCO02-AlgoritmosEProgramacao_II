lista1 = [1, 2, 3, 4]

print(1 in lista1)
print(10 in lista1)
print(2 not in lista1)
print(20 not in lista1)

lista2 = lista1 + [5, 6, -7, -8]
print(lista2)
lista2[0] = 1000
print(lista1)

lista2 = lista1
lista3 = [1, 2, 3, 4]

if(lista2 == lista3):
    print("Listas iguais")
else:
    print("Listas diferentes")
    
    
if(lista2 is lista3):
    print("Listas iguais")
else:
    print("Listas diferentes")
    
if(lista2 is lista1):
    print("Listas iguais")
else:
    print("Listas diferentes")
    
x = 3
y = 3

if x is y:
    print("São o mesmo objeto")
else:
    print("São objetos diferentes")
    
str1 = "hokama"
print(str1[0])
str1[0].upper()
print(str1)

lista2 = lista1 + [] # lista1.copy()
print(lista1)
lista1.append(5)
print(lista1)

if lista2 is lista1:
    print("Listas iguais")  
else: 
    print("Listas diferentes")
    
lista2.extend([6, 7, 8])
print(lista1)

### Tuplas
tupla1 = (10, 30, 20)
tupla2 = ("hokama", 10)
tupla3 = ("hokama", 10)

print(id(tupla2))
print(id(tupla3))
print(tupla2[1])

# tupla2[1] = 20 # Erro

print(tupla2[-1])
print(tupla1[1:])

valor = (10)
tupla4 = (10,)
print(type(valor))
print(type(tupla4))

lista6 = [1, 2]

lista6.extend((3, 4, 5))
print(lista6)



lista6.append((3, 4, 5))
print(lista6)
lista6[5] = 87
print(lista6)
print(lista6[5])
print(len(lista6))

print(min([1, 3, 4, 5, 5.9, 8.9]))

tupla6 = (1, 10) + (2, 20)
print(tupla6)

tupla7 = (1, 2, [3, 4])
print(id(tupla7))
tupla7[2][0] = 30
print(tupla7)