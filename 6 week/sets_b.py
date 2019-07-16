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

A1 = list(map(int, input().split()))
B1 = list(map(int, input().split()))


def Intersection(A, B):
    ans = [None] * (len(A) + len(B))
    i = len(A) - 1
    j = len(B) - 1
    k = 0
    while i >= 0 & j >= 0:
        if A[i] == B[j]:
            ans[k] = A[i]
            k += 1
            i -= 1
            j -= 1
        elif A[i] > B[j]:
            i -= 1
        else:
            j -= 1
    return [x for x in ans if x is not None]

print(*Intersection(A1, B1))
