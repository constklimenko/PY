"""Даны два списка, упорядоченных по возрастанию
(каждый список состоит из различных элементов).

Найдите пересечение множеств элементов этих списков,
то есть те числа, которые являются элементами
обоих списков. Алгоритм должен иметь сложность
 O(len(A)+len(B)).

Решение оформите в виде функции Intersection(A, B).
 Функция должна возвращать список пересечения
 данных списков в порядке возрастания элементов.
  Модифицировать исходные списки запрещается."""

NumList1 = list(map(int, input().split()))
NumList2 = list(map(int, input().split()))

if len(NumList1) > len(NumList2):
    answer = [None] * len(NumList2)
else:
    answer = [None] * len(NumList1)
i = 0
for x in NumList1:
    if NumList2.count(x):
        answer[i] = x
        i += 1
    else:
        pass

ans = [x for x in answer if x is not None]
print(*ans)
