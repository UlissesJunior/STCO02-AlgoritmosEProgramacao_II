# 📄 Bucket Sort

## 🔍 Como funciona
O **Bucket Sort** divide os elementos da lista em "baldes" com base em intervalos (por exemplo, faixas de valores). Cada balde é então ordenado individualmente, normalmente com Insertion Sort, e por fim todos os baldes são concatenados para formar a lista final ordenada.

## 📦 Complexidade de Espaço
- **O(n + k)** – sendo *n* o número de elementos e *k* o número de baldes.

## 📈 Análise Assintótica
- **Melhor caso:** O(n + k) — elementos uniformemente distribuídos e poucos elementos por balde.
- **Caso médio:** O(n + k)
- **Pior caso:** O(n²) — se todos os elementos caírem no mesmo balde e esse balde for ordenado com um algoritmo quadrático.

## 🔁 Exemplo de Iteração
Lista: `[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]`

- Distribuição em baldes (intervalos de 0.1):

  ```
  Bucket 0: []
  Bucket 1: [0.12, 0.17]
  Bucket 2: [0.21, 0.23, 0.26]
  Bucket 3: [0.39]
  Bucket 4: []
  Bucket 5: []
  Bucket 6: [0.68]
  Bucket 7: [0.72, 0.78]
  Bucket 8: []
  Bucket 9: [0.94]
  ```

- Ordenação dos baldes individualmente (usando Insertion Sort).
- Concatenação dos baldes:

  ```
  Resultado final: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
  ```

## 📊 Conjunto de Dados Ideal
- Dados **decimais** ou **floats**.
- Distribuição aproximadamente **uniforme** no intervalo [0, 1).
- Muito eficiente para listas grandes com essa característica.
