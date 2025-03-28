dicio_girias = {
    "gg": "good game",
    "hs": "head shot",
    "fb": "first blood",
    "smokar": "soltar fumacinha",
    "pinar": "errar todos os tiros"
}

print(dicio_girias["gg"])

dicio_girias["dronar"] = "soltar um drone"
print(dicio_girias["dronar"])
print(dicio_girias.get("dronar"))

# chave precisa ser imutável e hashavel

dicio_girias[1] = 'um'
dicio_girias[(2,3)] = "dois tres"

# lista é mutavel e nao hashavel
# dicio_girias[["gg", "hf"]] = "good game, have fun"

# essa tupla com uma lista
# embora imutavel, nao e hashavel
# dicio_girias[(1, [2, 3])] = "oi"

# operações
print("dronar" in dicio_girias)
print("ns" not in dicio_girias)

for (k,v) in dicio_girias.items():
    print(f'{k}: {v}')
    
print(list(dicio_girias.keys()))
print(list(dicio_girias.values()))

print(dicio_girias.popitem())

novo_dicio = {
    "ns": "nice shot",
    "TR": "terroristas",
    "CT": "contra-terroristas",
    "pinar": "hokama"
}

dicio_girias.update(novo_dicio)

print(len(dicio_girias))
dicio_girias.clear()
print(len(dicio_girias))

# Sets
# Não ordenado, sem repetições
# É de objetos hashaveis

s1 = {5, 4, 3, 2, 1}
s2 = set([2, 4, 6, 8, 10])

print(s1)

print(1 in s1)
print(1 in s2)

# União
print(s1 | s2)
print(s1.union(s2))

# Intersecção
print(s1 & s2)
print(s1.intersection(s2))

# Diferença (n simetrico)
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))

# Difereça simetrica
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

s3 = {1, 2}
print(s3.issubset(s1))
print(s3 <= s1)

print(s1.issuperset(s3))
print(s1 >= s3)

s1.add(6)
print(s1)
s1.remove(3)
print(s1)
print(s1.pop())

#frozenset
f1 = frozenset([1, 2, 3, 4, 5])
f2 = frozenset({2, 4, 6, 8, 10})

print(f1)
print(f2)

print(f1 | f2)
print(f1 & f2)

f1.add(6)
dicio_girias[f1] = "f1"

# from collections
# namedTuples
# defaultDict
# orderedDict
# chainmap
# counter
# userfict
# deque