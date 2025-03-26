# Aula 01

## Tipos de Variáveis
- int
- float
- complex
- str
- boolean

## Funções

### Bool

Função que verifica se o número é True ou False

```
x = 10
y = 0
bool(x) // TRUE
bool(y) // FALSE
```

### Range
Função que produz uma sequência de inteiros de começo ao fim, tem como default o step sendo 1

<b>Parâmetros = (start, end, step)</b>

```
for i in range(0, 10, 2):
    print(i) // 0, 2, 4, 6, 8
```

## Tipos Mutáveis e Imutáveis

### Lista
Passada como referência (Mutável)

```
def foo2(l):
    l[0] = l[0] + 1
    return

l = [1, 2, 3, 4]
foo2(l)
print(l) // [2, 2, 3, 4]
```

### Inteiro
Passado como valor (Imutável)

```
def foo(x):
    x = x + 1
    return

x = 1
foo(x)
print(x) // 1
```

### String
Passado como valor (Imutável)

```
str1 = "BANANA"
str2 = str1

str2 = str2.lower()
print(str1) //BANANA 
```