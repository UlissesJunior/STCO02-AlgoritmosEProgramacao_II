# Aula 03

## Big O Notation

<b>Entrada:</b> vetor A de tamanho N e um inteiro T
<b>Saída:</b> Verdadeiro se A contêm T, Falso no contrário

```
for k in range (1, n):
    if(A[k] == t):
        return True
    return False
```

<b>Resposta:</b> O(n)

</br>

<b>Entrada:</b> Dois vetores A e B de tamanho n e um inteiro T
<b>Saída:</b> Verdadeiro se A ou B contém T, Falso caso contrário

```
for k in range(1, n):
    if(A[k] == t):
        return True

for k in range(1, n):
    if(B[k] == t):
        return True

return False
```

<b>Resposta:</b> O(n)

</br>


<b>Entrada:</b> Dois vetores A e B de tamanho n
<b>Saída:</b> Verdadeiro se A ou B tem um número em comum, Falso caso contrário

```
for j in range(1, n):
    for k in range(1, n):
        if(A[j] == B[k]):
            return True
return False
```

<b>Resposta:</b> O(n²)

</br>

<b>Entrada:</b> Um vetor A de tamanho n
<b>Saída:</b> Verdadeiro se A tem números duplicados, Falso caso contrário

```
for j in range(1, n):
    for k in range(j+1, n):
        if(A[j] == A[k]):
            return True
return False
```

<b>Resposta:</b> O(n²)

## Hash Table

Ocupa mais memória que a linked list.
Tem o objetivo de inserir, buscar e excluir com O(1)