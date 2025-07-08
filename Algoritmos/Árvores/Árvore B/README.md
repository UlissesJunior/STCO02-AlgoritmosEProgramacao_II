
# 🌳 Árvore B – Explicação do Código

## ✅ O que é uma Árvore B?

A **Árvore B** é uma estrutura de dados auto-balanceada usada principalmente em sistemas de banco de dados e arquivos de sistema. Ela mantém os dados ordenados e permite buscas, inserções e remoções em tempo logarítmico.

### 🧩 Regras principais para uma árvore B de ordem `t`:

- Cada nó (exceto a raiz) contém no mínimo `t-1` chaves.
- Cada nó pode conter no máximo `2t-1` chaves.
- Um nó com `n` chaves possui `n+1` filhos.
- As chaves dentro de um nó são ordenadas.
- Todos os nós folha estão no mesmo nível.

---

## 🧠 Estrutura do Código

### 🔹 Classe `node`

```python
class node:
  def __init__(self):
    self.n = 0 
    self.folha = True
    self.chaves = []
    self.filhos = []
```

Cada nó possui:
- `n`: número de chaves atuais no nó.
- `folha`: se é um nó folha (`True` ou `False`).
- `chaves`: lista com as chaves do nó.
- `filhos`: lista com os ponteiros para os filhos.

---

## 🔍 Função de Busca

```python
def busca(x, k):
  i = 0
  while i < x.n and k > x.chaves[i]:
    i += 1
  if i < x.n and k == x.chaves[i]:
    return x.chaves[i]
  elif x.folha:
    return None
  else:
    return busca(x.filhos[i], k)
```

Busca recursivamente pela chave `k` na árvore B.

---

## 🧨 Quebra de Filho

```python
def quebrar_filho(pai, indice_filho):
  z = node()
  y = pai.filhos[indice_filho]
  z.folha = y.folha  
  pai.chaves.insert(indice_filho, y.chaves[t-1])
  z.chaves = y.chaves[t:]
  y.chaves = y.chaves[:t-1]
  pai.filhos.insert(indice_filho + 1, z)
  if not y.folha:
    z.filhos = y.filhos[t:]
    y.filhos = y.filhos[:t]
  pai.n += 1
  y.n = t-1
  z.n = t-1
```

Divide um filho `y` que está cheio (`2t - 1` chaves) em dois nós, inserindo a chave do meio no pai.

---

## ➕ Inserção em Nó Não Cheio

```python
def insere_nao_cheio(x, k):
  if x.folha:
    ...
  else:
    ...
```

Insere uma chave `k` num nó que **não está cheio**. Se necessário, quebra o filho antes de descer a recursão.

---

## 🌱 Inserção Geral

```python
def insere(raiz, k):
  if raiz.n == 2 * t - 1:
    raiz = quebrar_raiz(raiz)
  insere_nao_cheio(raiz, k)
  return raiz
```

Verifica se a raiz está cheia e, se sim, faz a quebra da raiz, criando uma nova raiz antes da inserção.

---

## 🌳 Quebra da Raiz

```python
def quebrar_raiz(raiz):
  s = node()
  s.folha = False
  s.n = 0
  s.filhos.append(raiz)
  quebrar_filho(s, 0)
  return s
```

Utilizada quando a raiz já está cheia e não pode receber mais chaves diretamente.

---

## 🖨️ Impressão da Árvore

```python
def imprime_arvore(raiz, nivel=0):
  for i in range(nivel):
    print("  ", end="")
  print(raiz.chaves)
  for filho in raiz.filhos:
    imprime_arvore(filho, nivel + 1)
```

Imprime a estrutura da árvore de forma indentada, representando os níveis hierárquicos.

---

## 🧪 Exemplo de Execução

1. Inicialização de árvore com `t = 3`
2. Inserções: `5, 4, 3, 2, 7, 8, 9, 10...`
3. Impressão após cada inserção
4. Quebra de nós automaticamente quando cheios
5. Quebra da raiz ao ultrapassar a capacidade

A árvore se reequilibra automaticamente e garante que todas as folhas estejam no mesmo nível, mantendo performance estável.

---