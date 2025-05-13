# 📄 Counting Sort

## 🔍 Como funciona
Conta quantas vezes cada valor aparece, soma cumulativamente e reconstrói a lista.

## 📦 Complexidade de Espaço
- **O(k + n)** – com *k* sendo o maior valor.

## 📈 Análise Assintótica
- **Todos os casos:** O(n + k)

## 🔁 Exemplo de Iteração
Lista: `[5, 3, 8, 4, 2]`
- Frequência: `[0, 0, 1, 1, 1, 1, 0, 0, 1]`
- Soma: `[0, 0, 1, 2, 3, 4, 4, 4, 4]`
- Resultado: `[2, 3, 4, 5, 8]`

## 📊 Conjunto de Dados Ideal
- Inteiros pequenos e não-negativos.
- Intervalo pequeno.