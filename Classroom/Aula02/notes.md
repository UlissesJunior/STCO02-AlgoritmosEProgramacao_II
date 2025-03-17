# Aula 02

## Tupla
É um objeto (Imutável)

### Diferença de tupla e valor
Por que quando eu imprimo uma tupla do jeito que está abaixo ele vai imprimir "(10,)" e não "(10)"?

```
tupla2 = ("hokama", 10)
print(tupla2[1:]) #(10,)
```

Basicamente isso se refere a uma artemanha visual em que o python precisa diferenciar uma tupla de 1 elemento de 1 valor, vide abaixo

```
valor = (10)
tupla4 = (10,)
print(type(valor)) #<class 'int'>
print(type(tupla4)) #<class 'tuple'>
```

### Extend e Append
O extend adiciona os valores de uma tupla pré criada em uma nova tupla e o append adiciona a tupla em si

```
lista6 = [1, 2]
lista6.extend((3, 4, 5))
print(lista6) # [1, 2, 3, 4, 5]

lista6.append((3, 4, 5))
print(lista6) # [1, 2, 3, 4, 5, (3, 4, 5)]
```