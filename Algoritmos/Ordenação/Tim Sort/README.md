# 📄 Tim Sort

## 🔍 Como funciona
Combinação de Insertion Sort e Merge Sort. Ordena blocos (runs) e depois mescla.

## 📦 Complexidade de Espaço
- **O(n)** – espaço extra para mesclagem.

## 📈 Análise Assintótica
- **Melhor caso:** O(n)
- **Médio e pior:** O(n log n)

## 🔁 Exemplo de Iteração
Lista: `[5, 3, 8, 4, 2]`
- Runs: `[5, 3]`, `[8, 4, 2]`
- Ordena: `[3, 5]`, `[2, 4, 8]`
- Mescla: `[2, 3, 4, 5, 8]`

## 📊 Conjunto de Dados Ideal
- Listas parcialmente ordenadas.
- Listas grandes.