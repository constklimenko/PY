"""Даны два целочисленных списка A и B,
 упорядоченных по неубыванию.
  Объедините их в один упорядоченный список С
   (то есть он должен содержать len(A)+len(B)
   элементов). Решение оформите в виде функции
    merge(A, B), возвращающей новый список.
     Алгоритм должен иметь сложность O(len(A)+len(B)).
      Модифицировать исходные списки запрещается.
       Использовать функцию sorted и метод sort
        запрещается."""

NumList1 = list(map(int, input().split()))
NumList2 = list(map(int, input().split()))


def merge(A, B):
    i, j, C = 0, 0, []
    for _ in range(len(A) + len(B)):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        elif i < len(A):
            C.append(A[i])
            i += 1
        elif j < len(B):
            C.append(B[j])
            j += 1
    return C


answer = merge(NumList2, NumList1)

print(*answer)
