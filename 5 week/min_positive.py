"""Выведите значение наименьшего из всех
положительных элементов в списке.
Известно, что в списке есть хотя бы один
положительный элемент, а значения всех элементов списка
 по модулю не превосходят 1000."""

numList = list(map(int, input().split()))
minPositive = 1000

for x in range(len(numList)):
    if numList[x] > 0:
        if numList[x] <= minPositive:
            minPositive = numList[x]

print(minPositive)
