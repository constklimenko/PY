"""Даны вещественные числа a, b, c, d, e, f.
 Известно, что система линейных уравнений:

ax + by = e

cx + dy = f

имеет ровно одно решение.
 Выведите два числа x и y,
 являющиеся решением этой системы."""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = 0
y = 0


def f2(k, l, m, i):
    return (m - l * i) / k

if a == 0:
    y = e / b
    if c != 0:
        x = f2(c, d, f, y)
    else:
        print("no answer")
elif c == 0:
    y = f / d
    if a != 0:
        x = f2(a, b, e, y)
    else:
        print("no answer")
elif b == 0:
    x = e/a
    if d != 0:
        y = f2(d, c, f, x)
    else:
        print("no answer")
elif d == 0:
    x = f/c
    if b != 0:
        y = f2(b, a, e, x)
    else:
        print("no answer")

else:
    if ((a * d) / c - b) == 0:
        y = (f + d - (e * c) / a) / d
        x = (e / a - d / c) * y
    else:
        y = ((a * f) / c - e) / ((a * d) / c - b)
        x = (f - d * y) / c
print(x, y)
