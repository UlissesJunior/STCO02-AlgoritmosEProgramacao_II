# 📄 Selection Sort

## 🔍 Como funciona
O **Selection Sort** encontra o menor elemento e o coloca na posição correta, repetindo para o restante da lista.

## 📦 Complexidade de Espaço
- **O(1)** – Algoritmo in-place.

## 📈 Análise Assintótica
- **Todos os casos:** O(n²)

## 🔁 Exemplo de Iteração
Lista: `[5, 3, 8, 4, 2]`
- Passo 1: `[2, 3, 8, 4, 5]`
- Passo 2: `[2, 3, 8, 4, 5]`
- Passo 3: `[2, 3, 4, 8, 5]`
- Passo 4: `[2, 3, 4, 5, 8]`

## 🧮 Iteração Detalhada

### Lista original:
`[5, 3, 8, 4, 2]`

O algoritmo percorre a lista procurando o menor elemento e o coloca na posição correta a cada iteração.

### Iteração 1 (i = 0):
- Sublista analisada: `[5, 3, 8, 4, 2]`  
- Menor elemento: `2` (índice 4)  
- Troca 5 com 2  
**Resultado:** `[2, 3, 8, 4, 5]`

### Iteração 2 (i = 1):
- Sublista analisada: `[3, 8, 4, 5]`  
- Menor elemento: `3` (índice 1)  
- Nenhuma troca necessária  
**Resultado:** `[2, 3, 8, 4, 5]`

### Iteração 3 (i = 2):
- Sublista analisada: `[8, 4, 5]`  
- Menor elemento: `4` (índice 3)  
- Troca 8 com 4  
**Resultado:** `[2, 3, 4, 8, 5]`

### Iteração 4 (i = 3):
- Sublista analisada: `[8, 5]`  
- Menor elemento: `5` (índice 4)  
- Troca 8 com 5  
**Resultado:** `[2, 3, 4, 5, 8]`


## 📊 Conjunto de Dados Ideal
- Listas pequenas.