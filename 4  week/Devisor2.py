n = int(input())


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

print(MinDivisor(n))
