# 📄 README - Radix Sort

## 🔍 Como funciona
Ordena elementos dígito por dígito, começando do menos significativo. Usa Counting Sort como sub-rotina.

## 📦 Complexidade de Espaço
- **O(n + k)** – onde k é o valor do dígito (geralmente 10).

## 📈 Análise Assintótica
- **Todos os casos:** O(nk)

## 🔁 Exemplo de Iteração
Lista: `[170, 45, 75, 90, 802, 24, 2, 66]`

1. Ordena por unidades: `[170, 90, 802, 2, 24, 45, 75, 66]`
2. Ordena por dezenas: `[802, 2, 24, 45, 66, 170, 75, 90]`
3. Ordena por centenas: `[2, 24, 45, 66, 75, 90, 170, 802]`

## 📊 Conjunto de Dados Ideal
- Muitos inteiros com poucos dígitos fixos.