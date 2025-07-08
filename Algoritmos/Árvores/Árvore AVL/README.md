
# 🌳 Árvore AVL – Explicação do Código

## ✅ O que é uma Árvore AVL?

A Árvore AVL (Adelson-Velsky e Landis) é uma **árvore binária de busca autobalanceada**.  
Ela mantém a diferença de altura entre as subárvores de cada nó em no máximo 1.

**Fator de balanceamento (FB):**

```
FB = altura da subárvore esquerda - altura da subárvore direita
```

Se o FB for maior que 1 ou menor que -1, a árvore está **desequilibrada** e precisa ser **rotacionada**.

---

## 🧠 Estrutura do Código

### 🔹 Classe `node`

```python
class node:
  def __init__(self, dado):
    self.dado = dado
    self.esq = None
    self.dir = None
    self.altura = 0
```

Cada nó guarda:
- `dado`: valor armazenado
- `esq`: filho esquerdo
- `dir`: filho direito
- `altura`: altura do nó

---

### 🔹 Função `altura`

```python
def altura(y):
  if y == None:
    return -1
  return y.altura
```

Retorna a altura de um nó ou -1 se for `None`.

---

### 🔹 Rotações

#### 🔸 Rotação à Direita

```python
def rotacaoDireita(y):
  x = y.esq
  y.esq = x.dir
  x.dir = y
  ...
  return x
```

Usada no caso **esquerda-esquerda (FB = 2)**.

#### 🔸 Rotação à Esquerda

```python
def rotacaoEsquerda(y):
  x = y.dir
  y.dir = x.esq
  x.esq = y
  ...
  return x
```

Usada no caso **direita-direita (FB = -2)**.

---

### 🔹 Fator de Balanceamento (FB)

```python
def fb(y):
  return altura(y.esq) - altura(y.dir)
```

---

### 🔹 Inserção com balanceamento

```python
def insere(y, dado):
  if y is None:
    return node(dado)

  if dado < y.dado:
    y.esq = insere(y.esq, dado)
    if fb(y) == 2:
      if dado > y.esq.dado:
        y.esq = rotacaoEsquerda(y.esq)
      y = rotacaoDireita(y)
  elif dado > y.dado:
    y.dir = insere(y.dir, dado)
    if fb(y) == -2:
      if dado < y.dir.dado:
        y.dir = rotacaoDireita(y.dir)
      y = rotacaoEsquerda(y)
  else:
    print("dado igual")
    return y

  y.altura = max(altura(y.esq), altura(y.dir)) + 1
  return y
```

---

## 🔁 Exemplo de inserção

```python
T = None
T = insere(T, 33)
T = insere(T, 42)
T = insere(T, 49)
```

### 🌲 Resultado (após balanceamento):

```
    42
   /  \
  33  49
```

---

## 🖨️ Impressão da árvore

```python
def imprime(arvore, nivel=0, prefixo="Raiz: "):
    if arvore is not None:
        print(" " * (4 * nivel) + prefixo + str(arvore.dado))
        imprime(arvore.esq, nivel + 1, "E: ")
        imprime(arvore.dir, nivel + 1, "D: ")
```

### Saída esperada:

```
Raiz: 42
    E: 33
    D: 49
```

---