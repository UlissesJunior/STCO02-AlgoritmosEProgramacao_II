# 📄 Bubble Sort

## 🔍 Como funciona
O **Bubble Sort** compara elementos adjacentes e os troca de posição se estiverem fora de ordem. Esse processo se repete até que a lista esteja ordenada.

## 📦 Complexidade de Espaço
- **O(1)** – É um algoritmo in-place, não requer espaço adicional significativo.

## 📈 Análise Assintótica
- **Melhor caso:** O(n)
- **Caso médio:** O(n²)
- **Pior caso:** O(n²)

## 🔁 Exemplo de Iteração
Lista: `[5, 3, 8, 4, 2]`
- Passo 1: `[3, 5, 8, 4, 2]`
- Passo 2: `[3, 5, 4, 8, 2]`
- Passo 3: `[3, 5, 4, 2, 8]`
- Continua até ordenado.

## 📊 Conjunto de Dados Ideal
- Listas pequenas (até ~100 elementos).
- Listas quase ordenadas.