A1 = list(map(int, input().split()))
B1 = list(map(int, input().split()))


def Intersection(A, B):
    C1 = set(A) & set(B)

    C = list(C1)
    C.sort()
    return C


print(*Intersection(A1, B1))
