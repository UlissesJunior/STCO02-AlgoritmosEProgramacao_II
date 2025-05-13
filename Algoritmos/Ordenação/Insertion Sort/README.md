# 📄 Insertion Sort

## 🔍 Como funciona
O **Insertion Sort** insere elementos um a um na posição correta de uma sublista ordenada.

## 📦 Complexidade de Espaço
- **O(1)** – Algoritmo in-place.

## 📈 Análise Assintótica
- **Melhor caso:** O(n)
- **Caso médio e pior caso:** O(n²)

## 🔁 Exemplo de Iteração
Lista: `[5, 3, 8, 4, 2]`
- Passo 1: `[3, 5, 8, 4, 2]`
- Passo 2: `[3, 5, 8, 4, 2]`
- Passo 3: `[3, 4, 5, 8, 2]`
- Passo 4: `[2, 3, 4, 5, 8]`

## 🧮 Iteração Detalhada

### Lista original:
`[5, 3, 8, 4, 2]`

O algoritmo começa do segundo elemento (índice 1), comparando e inserindo com base na sublista ordenada à esquerda.

### Iteração 1 (i = 1, chave = 3):
- Compara com 5 → 3 < 5 → move 5 para a direita  
- Insere 3 na posição 0  
**Resultado:** `[3, 5, 8, 4, 2]`

### Iteração 2 (i = 2, chave = 8):
- Compara com 5 → 8 > 5 → nada muda  
**Resultado:** `[3, 5, 8, 4, 2]`

### Iteração 3 (i = 3, chave = 4):
- Compara com 8 → 4 < 8 → move 8  
- Compara com 5 → 4 < 5 → move 5  
- Insere 4 na posição 1  
**Resultado:** `[3, 4, 5, 8, 2]`

### Iteração 4 (i = 4, chave = 2):
- Compara com 8 → move 8  
- Compara com 5 → move 5  
- Compara com 4 → move 4  
- Compara com 3 → move 3  
- Insere 2 na posição 0  
**Resultado:** `[2, 3, 4, 5, 8]`


## 📊 Conjunto de Dados Ideal
- Listas pequenas ou quase ordenadas.