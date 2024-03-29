"""Дан список из N (N≤2*10⁵) элементов,
 которые принимают целые значения от 0 до 100.

Отсортируйте этот список в порядке неубывания
элементов. Выведите полученный список.

Решение оформите в виде функции CountSort(A),
 которая модифицирует передаваемый ей список.
  Использовать встроенные функции сортировки нельзя."""

NumList = list(map(int, input().split()))


def CountSort(A):
    a = [0] * 101
    for x in A:
        a[int(x)] += 1
    return a


b = CountSort(NumList)

for y in range(len(b)):
    print((str(y) + " ") * int(b[y]), end="")
