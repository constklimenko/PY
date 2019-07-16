"""Выведите значение наименьшего нечетного
элемента списка, гарантируется, что хотя бы
один нечётный элемент в списке есть."""

numList = list(map(int, input().split()))

minOdd = 0

for x in numList:
    if x % 2:
        if minOdd == 0:
            minOdd = x
        elif x < minOdd:
            minOdd = x
        else:
            continue

print(minOdd)
