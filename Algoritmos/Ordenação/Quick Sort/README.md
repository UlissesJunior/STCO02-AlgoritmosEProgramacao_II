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

## 📊 Conjunto de Dados Ideal
- Listas grandes com elementos distintos.