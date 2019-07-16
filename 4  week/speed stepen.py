def chet_pow(a, n):
    if n == 0:
        return 1
    elif n == 2:
        return a * a
    else:
        return pw(a, n / 2)**2


def nechet_pow(a, n):
    if n == 1:
        return a
    else:
        return a * chet_pow(a, n - 1)


def pw(a, n):
    if a != 0:
        if n % 2 == 0:
            return chet_pow(a, n)

        else:
            return nechet_pow(a, n)

    else:
        return 0


a = float(input())
n = int(input())

print(pw(a, n))
