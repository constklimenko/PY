def power(a, n):
    if n == 1:
        return a
    elif n > 1:
        return a * power(a, n - 1)
    elif n == 0:
        return 1


a = float(input())
n = int(input())

print(power(a, n))
