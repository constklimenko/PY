"""Переставьте соседние элементы списка
 (A[0] c A[1],A[2] c A[3] и т.д.).
 Если элементов нечетное число,
то последний элемент остается на своем месте."""

numList = list(map(int, input().split()))

for x in range(0, (len(numList) // 2) * 2, 2):
    numList[x], numList[x + 1] = numList[x + 1], numList[x]

print(" ".join(map(str, numList)))
