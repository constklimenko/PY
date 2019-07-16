n = int(input())


def MinDivisor(n):
    if n % 2 == 0:
        return 2

    lst = [2]
    dev = 0

    for i in range(3, n + 1, 2):
        if dev:
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

print(MinDivisor(n))
