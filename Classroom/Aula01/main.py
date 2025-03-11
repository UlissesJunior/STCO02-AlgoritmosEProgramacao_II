z = 0.00000000000000000000005
print(z)
z = z + 1
z = z - 1
print(z)
print('')

str1 = 'Hokama'
str2 = "STCO02"
str3 = """String com 
varias linhas"""
str4 = str1*3
print(str3)
print(str4)
print('')

lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]
lista3 = [1, 2, 3, "a", "b", 'c', lista1]
print(lista3)
print('')

def foo(x):
    x = x + 1
    return

x = 1
foo(x)
print(x)

def foo2(l):
    l[0] = l[0] + 1
    return

l = [1, 2, 3, 4]
foo2(l)
print(l)
print('')

str1 = "Banana"
str2 = str1
print(id(str1))
print(id(str2))

str2 = str2.lower()
print('')

lista1= ["B", "a", "n", "a", "n", "a"]
lista2 = lista1
lista2[0] = "b"

print(lista1)
print('')

for i in range(0,10,2):
    print(i)
print('')

# x = 0
# for i in range(0,10_000_000,1):
#     x = x + 1

# print(x)

# x=0
# lista1 = list(range(0,10_000_000,1))
# for i in lista1:
#     x = x + 1
# print(x)

lista1 = [1, 2, 3, 4, 5]
lista2 = lista1[2:]
print(lista2)
print(lista1[1])
print(lista1[-1])

lista2[0] = 100
print(lista1)

lista1 = [1,2,3,4]
lista2 = lista1[0:]
print(id(lista1))
print(id(lista2))
print('')

print(2 in lista1)