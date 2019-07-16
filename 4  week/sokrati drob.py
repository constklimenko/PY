"""Даны два натуральных числа n и m.

Сократите дробь (n / m), то есть
выведите два других числа p и q таких,
 что (n / m) = (p / q) и дробь (p / q)
 — несократимая.

Решение оформите в виде функции
 ReduceFraction(n, m), получающая значения
 n и m и возвращающей кортеж из двух
 чисел (return p, q)."""
from math import sqrt


def MinDivisor(n):
    if n < 1:
        return -1

    if n == 1:
        return 1

    if n % 2 == 0:
        return 2

    lst = [2]
    dev = 0

    for i in range(3, int(n + 1), 2):
        if dev:
            break
        if i > 7 & i > sqrt(n) + 2:
            break
        elif (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                if n % i == 0:
                    dev = i

                break
            if (i % j == 0):
                break
            else:
                lst.append(i)
                if n % i == 0:
                    dev = i

    return dev


def getDivisorsList(n):
    lst = []
    num = n
    while num > 1:
        md = int(MinDivisor(num))
        lst.append(md)
        num = int(num / md)
    return lst


def ReduceFraction(n, m):
    DLm = getDivisorsList(m)
    DLn = getDivisorsList(n)
    DL = list(set(DLm) & set(DLn))

    if not DL:
        return (int(n), int(m))

    for x in DL:
        n = n / x
        m = m / x

    DLm = getDivisorsList(m)
    DLn = getDivisorsList(n)
    DL = list(set(DLm) & set(DLn))

    if not DL:
        return (int(n), int(m))

    else:
        return ReduceFraction(n, m)


n = int(input())
m = int(input())

print(ReduceFraction(n, m)[0], ReduceFraction(n, m)[1])
