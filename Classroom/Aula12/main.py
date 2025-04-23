k = 8
A = [3, 4, 2, 1, 8, 0]

C = [0 for _ in range(0, k + 1)]

for a in A:
    C[a] += 1

for i in range(1, k + 1):
    C[i] = C[i] + C[i - 1]

print(C)

B = [None for _ in range(0, len(A))]
print(B)

for a in A:
    B[C[a] - 1] = a

print(B)


def CountingSort(A, k):
    B = [None for _ in range(0, len(A))]
    C = [0 for _ in range(0, k + 1)]
    for a in A:
        C[a] += 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    for a in A:
        a = A[i]
        B[C[a] - 1] = a
        C[a] -= 1
    return B


k = 1_000_000
n = 1_000_000
A = [3, 3, 4, 2, 1, 8, 0, 1]

import random

A = [random.randInt(0, k) for _ in range(0, n)]

B = CountingSort(A, k)