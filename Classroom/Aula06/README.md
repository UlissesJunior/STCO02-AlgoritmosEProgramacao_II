# Aula 6 - Estruturas de Dados Avançadas

Nesta aula, exploramos os dicionários (`dict`) e conjuntos (`set`), além de algumas estruturas do módulo `collections`, que fornecem versões otimizadas e especializadas de tipos padrão do Python.

---

## Dicionários (`dict`)

Os dicionários são estruturas que armazenam pares `chave: valor`, onde as chaves precisam ser imutáveis e hasháveis.

### Criando e acessando um dicionário
```python
dicio_girias = {
    "gg": "good game",
    "hs": "head shot",
    "fb": "first blood"
}

print(dicio_girias["gg"])  # good game
```

### Adicionando elementos
```python
dicio_girias["dronar"] = "soltar um drone"
print(dicio_girias["dronar"])  # soltar um drone
```

### Verificando a existência de chaves
```python
print("dronar" in dicio_girias)  # True
print("ns" not in dicio_girias)  # True
```

### Iterando sobre um dicionário
```python
for k, v in dicio_girias.items():
    print(f'{k}: {v}')
```

### Obtendo chaves e valores
```python
print(list(dicio_girias.keys()))  # ['gg', 'hs', 'fb', 'dronar']
print(list(dicio_girias.values()))  # ['good game', 'head shot', 'first blood', 'soltar um drone']
```

### Removendo elementos
```python
print(dicio_girias.popitem())  # Remove e retorna o último item
```

### Atualizando um dicionário
```python
novo_dicio = {
    "ns": "nice shot",
    "TR": "terroristas",
    "CT": "contra-terroristas"
}

dicio_girias.update(novo_dicio)
print(len(dicio_girias))  # Número total de elementos
```

### Limpando um dicionário
```python
dicio_girias.clear()
print(len(dicio_girias))  # 0
```

---

## Conjuntos (`set`)

Os conjuntos são coleções desordenadas de elementos únicos e hasháveis.

### Criando conjuntos
```python
s1 = {5, 4, 3, 2, 1}
s2 = set([2, 4, 6, 8, 10])

print(s1)  # {1, 2, 3, 4, 5}
```

### Verificando a existência de elementos
```python
print(1 in s1)  # True
print(1 in s2)  # False
```

### Operações com conjuntos
#### União
```python
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 8, 10}
print(s1.union(s2))
```

#### Interseção
```python
print(s1 & s2)  # {2, 4}
print(s1.intersection(s2))
```

#### Diferença
```python
print(s1 - s2)  # {1, 3, 5}
print(s1.difference(s2))
```
```python
print(s2 - s1)  # {6, 8, 10}
print(s2.difference(s1))
```

#### Diferença simétrica
```python
print(s1 ^ s2)  # {1, 3, 5, 6, 8, 10}
print(s1.symmetric_difference(s2))
```

### Subconjuntos e superconjuntos
```python
s3 = {1, 2}
print(s3.issubset(s1))  # True
print(s1.issuperset(s3))  # True
```

### Modificando conjuntos
```python
s1.add(6)
print(s1)  # {1, 2, 3, 4, 5, 6}
```
```python
s1.remove(3)
print(s1)  # {1, 2, 4, 5, 6}
```
```python
print(s1.pop())  # Remove e retorna um elemento aleatório
```

---

## `frozenset`

O `frozenset` é uma versão imutável de um conjunto (`set`).

```python
f1 = frozenset([1, 2, 3, 4, 5])
f2 = frozenset({2, 4, 6, 8, 10})

print(f1 | f2)  # União
print(f1 & f2)  # Interseção
```

---

## Estruturas do módulo `collections`

### 1. Named Tuples (`namedtuple`)
```python
from collections import namedtuple

Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
p1 = Pessoa(nome='Carlos', idade=25)
print(p1.nome)  # Carlos
```

### 2. DefaultDict (`defaultdict`)
```python
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d['a'])  # 1
```

### 3. OrderedDict (`OrderedDict`)
```python
from collections import OrderedDict

d = OrderedDict()
d['b'] = 2
d['a'] = 1
d['c'] = 3
print(d)  # OrderedDict([('b', 2), ('a', 1), ('c', 3)])
```

### 4. ChainMap (`ChainMap`)
```python
from collections import ChainMap

defaults = {'cor': 'azul', 'tamanho': 'M'}
usuario = {'tamanho': 'G'}
config = ChainMap(usuario, defaults)
print(config['cor'])  # azul
```

### 5. Counter (`Counter`)
```python
from collections import Counter

frase = "banana"
c = Counter(frase)
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})
```

### 6. UserDict (`UserDict`)
```python
from collections import UserDict

class MeuDicionario(UserDict):
    def __setitem__(self, key, value):
        print(f'Salvando {key}: {value}')
        super().__setitem__(key, value)

d = MeuDicionario()
d['teste'] = 123
```

### 7. Deque (`deque`)
```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
d.pop()
d.popleft()
print(d)  # deque([1, 2, 3])
```