"""Циклически сдвиньте элементы
 списка вправо(A[0] переходит на место A[1], A[1]
  на место A[2], ...,
последний элемент переходит на место A[0])."""

numList = list(map(int, input().split()))

numList.insert(0, numList.pop())

print(" ".join(map(str, numList)))
