# 📄 Quick Sort

## 🔍 Como funciona
Escolhe um pivô, particiona a lista em elementos menores e maiores, e ordena recursivamente.

## 📦 Complexidade de Espaço
- **O(log n)** – devido à recursão.

## 📈 Análise Assintótica
- **Melhor/médio caso:** O(n log n)
- **Pior caso:** O(n²)

## 🔁 Exemplo de Iteração
Lista: `[5, 3, 8, 4, 2]`
- Pivô: 5 → `[3, 4, 2]`, `[8]`
- Ordena: `[2, 3, 4]`
- Resultado: `[2, 3, 4, 5, 8]`

## 🧮 Iteração Detalhada

### Lista original:
`[5, 3, 8, 4, 2]`

Utilizando o primeiro elemento como pivô (variações existem), o algoritmo segue particionando e ordenando recursivamente.

### Primeira chamada (lista = `[5, 3, 8, 4, 2]`)
- **Pivô:** 5  
- Menores que o pivô: `[3, 4, 2]`  
- Maiores que o pivô: `[8]`  
- Recursão em `[3, 4, 2]` e `[8]`

### Segunda chamada (lista = `[3, 4, 2]`)
- **Pivô:** 3  
- Menores que o pivô: `[2]`  
- Maiores que o pivô: `[4]`  
- Recursão em `[2]` e `[4]`  
- Como `[2]` e `[4]` têm apenas 1 elemento, já estão ordenadas  
- Combina: `[2, 3, 4]`

### Terceira chamada (lista = `[8]`)
- Apenas um elemento → já está ordenado

### Combinação final:
- `[2, 3, 4] + [5] + [8]`  
**Resultado:** `[2, 3, 4, 5, 8]`

## 📊 Conjunto de Dados Ideal
- Listas grandes com elementos distintos.