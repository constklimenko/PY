"""def IsPrime(n):
    if n == 1 or n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)), 2):
            if n % i == 0:
                return False
        return True"""
from math import sqrt


def MinDivisor(n):
    if n % 2 == 0:
        return 2

    dev = 0

    for i in range(3, n + 1, 2):
        if dev:
            break
        elif i * i > n:
            break
        elif n % i == 0:
            dev = i
    if dev == 0:
        dev = n
    return dev


n = int(input())

if MinDivisor(n) == -1:
    print("вы ввели не натуральное число")

elif n == MinDivisor(n):
    print("YES")
else:
    print("NO")
