
# 🌳 Árvore Rubro-Negra – Explicação do Código

## ✅ O que é uma Árvore Rubro-Negra?

A **Árvore Rubro-Negra** (Red-Black Tree) é uma **árvore binária de busca autobalanceada** que garante inserções, buscas e remoções em tempo **O(log n)**.

Cada nó pode ser **vermelho ou negro**, e a estrutura garante que não existam caminhos demasiadamente longos à esquerda ou direita.

---

## 📏 Propriedades da Árvore Rubro-Negra

1. Todo nó é **vermelho** ou **negro**.
2. A raiz é sempre **negra**.
3. Nenhum nó vermelho pode ter um filho vermelho (ou seja, dois vermelhos consecutivos são proibidos).
4. Todo caminho de um nó até uma folha contém o **mesmo número de nós negros**.

---

## 🧠 Estrutura do Código

### 🔹 Classe `noh`

```python
class noh:
  def __init__(self, dado):
    self.dado = dado
    self.esq = None
    self.dir = None
    self.cor = True  # True para vermelho, False para negro
```

Cada nó armazena:
- `dado`: o valor.
- `esq`: ponteiro para o filho esquerdo.
- `dir`: ponteiro para o filho direito.
- `cor`: `True` se for vermelho, `False` se for negro.

---

## 🔄 Rotações

### 🔸 Rotação à esquerda

```python
def rotacionaEsquerda(x):
  y = x.dir
  x.dir = y.esq
  y.esq = x
  y.cor = x.cor
  x.cor = True 
  return y
```

Corrige casos onde há um nó vermelho à direita (violando a regra da esquerda-preferência).

### 🔸 Rotação à direita

```python
def rotacionaDireita(x):
  y = x.esq
  x.esq = y.dir
  y.dir = x
  y.cor = x.cor
  x.cor = True
  return y
```

Corrige quando dois vermelhos consecutivos aparecem à esquerda.

---

## 🔺 Subida de Vermelho

```python
def sobeVermelho(x):
  x.cor = True
  x.esq.cor = False
  x.dir.cor = False
  return x
```

Usado quando ambos os filhos são vermelhos: promove o vermelho para o pai.

---

## 🩸 Checagem de cor

```python
def ehVermelho(x):
  if x == None:
    return False
  return x.cor

def ehNegro(x):
  if x == None:
    return True
  return x.cor == False
```

Essas funções evitam erros com `None` e ajudam nas verificações de balanceamento.

---

## ➕ Inserção

### Função auxiliar recursiva:

```python
def insere_aux(raiz, dado):
  if raiz == None:
    return noh(dado)
  elif dado < raiz.dado:
    raiz.esq = insere_aux(raiz.esq, dado)
  elif dado > raiz.dado:
    raiz.dir = insere_aux(raiz.dir, dado)
  else:
    return raiz

  if ehVermelho(raiz.dir) and ehNegro(raiz.esq):
    raiz = rotacionaEsquerda(raiz)
  if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
    raiz = rotacionaDireita(raiz)
  if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
    sobeVermelho(raiz)
  return raiz
```

### Inserção externa

```python
def insere(raiz, dado):
  raiz = insere_aux(raiz, dado)
  raiz.cor = False  # a raiz sempre deve ser negra
  return raiz
```

---

## 🖨️ Impressão da Árvore

```python
def imprime(A):
  if A == None:
    return
  print('(', end='')
  imprime(A.esq)
  print(',', end='')
  print(A.dado, end=',')
  imprime(A.dir)
  print(')', end='')
```

Mostra a árvore no formato de parênteses aninhados.

---

## 🧪 Exemplo de uso

```python
A = None
A = insere(A, 7)
A = insere(A, 5)
A = insere(A, 9)
A = insere(A, 3)
A = insere(A, 1)
A = insere(A, 2)
imprime(A)
```

A árvore se reequilibra automaticamente a cada inserção, aplicando rotações e recolorindo quando necessário.

---

Se quiser adicionar remoção ou visualização com cores, posso ajudar com isso também!
