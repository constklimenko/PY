def sum(a, n):
    if n == 0:
        return a
    elif n == 1:
        return a + 1
    else:
        return a + sum(1, n - 1)


a = int(input())
n = int(input())

print(sum(a, n))
