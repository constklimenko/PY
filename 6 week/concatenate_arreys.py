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


def merge(A: list, B: list):
    c = []
#    x = 0
    if len(A) > len(B):
        x = 2 * len(B)
    else:
        x = 2 * len(A)
#    print(x)
    while x > 0:
        #        print(x)
        if not B:
            break
#            while len(A):
#                c.append(A.pop(0))
#                x -= 1
        elif not A:
            break
#            while len(B):
#                c.append(B.pop(0))
#                x -= 1
        elif A[0] < B[0]:
            c.append(A.pop(0))
            x -= 1
#            print(B)
        elif A[0] == B[0]:
            c.append(A.pop(0))
            c.append(B.pop(0))
            x -= 2
#            print(B)
        else:
            c.append(B.pop(0))
            x -= 1
#            print(B)

#    print("len A =", len(A), "len B = ", len(B))
    while len(A):
        c.append(A.pop(0))
    while len(B):
        c.append(B.pop(0))
    return c

answer = merge(NumList2, NumList1)

print(*answer)
