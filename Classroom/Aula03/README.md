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

Uma aplicação de hashTable pode ser:

```
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None for i in range(size)]
        self.count = 0
        
    def hash(self, s):
        mult = 1
        hashValue = 0
        for c in s:
            hashValue += mult * ord(c)
            mult += 1
        return hashValue
    
    def put(self, key, value):
        hv = self.hash(key) % self.size
        hi = HashItem(key, value)

        while self.slots[hv] != None:
            hv = (hv + 1) % self.size
        
        self.slots[hv] = hi
        self.count +=1
        self.check_growth()
        
    def get(self, key):
        hv = self.hash(key) % self.size
        while self.slots[hv] != None:
            if self.slots[hv].key == key:
                return self.slots[hv].value
            hv = (hv + 1) % self.size
        
        return None
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def growth(self):
        newTable = HashTable(self.size * 2)
        for i in range(0, self.size):
            if self.slots[i] != None:
                newTable.put(self.slots[i].key, self.slots[i].value)
        self.size = self.size * 2
        self.slots = newTable.slots
        
    def check_growth(self):
        fatorCarga = self.count / self.size
        if fatorCarga > 0.65:
            self.growth()
```

### Sondagem Linear
Aplicação mais básica no HashTable

```hv = hv + 1```

Utilização na classe HashTable:

```
    def put(self, key, value):
        hv = self.hash(key) % self.size
        hi = HashItem(key, value)

        while self.slots[hv] != None:
            hv = (hv + 1) % self.size
        
        self.slots[hv] = hi
        self.count +=1
        self.check_growth()
        
    def get(self, key):
        hv = self.hash(key) % self.size
        while self.slots[hv] != None:
            if self.slots[hv].key == key:
                return self.slots[hv].value
            hv = (hv + 1) % self.size
        
        return None

    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
```

### Sondagem Quadrática
A sondagem quadrática é uma técnica de resolução de colisão em tabelas hash. Não vai tratar casos iguais.

```hv = hv + i^2 % size```

Para aplicar é necessário substituir a função get e put do HashTable por:

```
    def put_quadratico(self, key, value):
        hi = HashItem(key, value)
        hv = self.hash(key) % self.size
        pos = hv
        
        i = 1
        
        while self.slots[pos] != None:
            pos = (hv + pow(i, 2)) % self.size
            i = i + 1
        
        self.slots[pos] = hi
        self.count +=1
        self.check_growth()
        
    def get_quadratico(self, key):
        hv = self.hash(key) % self.size
        pos = hv
        i = 1
        while self.slots[pos] != None:
            if self.slots[pos].key == key:
                return self.slots[pos].value
            pos = (hv + pow(i, 2)) % self.size
            i = i + 1
        
        return None

    def __setitem__(self, key, value):
        self.put_quadratico(key, value)
    
    def __getitem__(self, key):
        return self.get_quadratico(key)
    
```

### Double Hashing

Técnica para aplicar o hash 2 vezes

Primo = Qualquer valor primo q seja menor q o tamanho da tabela

```
def hash1(key):
    return key % size

def hash2(key):
    primo = 5  
    num = hash1(key)
    return primo - (num % primo)

hashValue = hv + i * hash2(key) % size 
```

Aplicação na classe HashTable:

```
    def hash(self, s):
        mult = 1
        hashValue = 0
        for c in s:
            hashValue += mult * ord(c)
            mult += 1
        return hashValue
    def hash2(self, key):
        num = self.hash(key)
        prime = 5
        return prime - (num % prime)
        
    def put_doublehash(self, key, value):
        hi = HashItem(key, value)
        hv = self.hash(key) % self.size
        pos = hv
        
        i = 1
        
        while self.slots[pos] != None:
            pos = (hv + i * self.hash2(key)) % self.size
            i += 1
        
        self.slots[pos] = hi
        self.count +=1
        self.check_growth()
        
    def get_doublehash(self, key):
        hv = self.hash(key) % self.size
        pos = hv
        i = 1
        while self.slots[pos] != None:
            if self.slots[pos].key == key:
                return self.slots[pos].value
            pos = (hv + i * self.hash2(key)) % self.size
            i += 1
        
        return None

    def __setitem__(self, key, value):
        self.put_doublehash(key, value)
    
    def __getitem__(self, key):
        return self.get_doublehash(key)
```