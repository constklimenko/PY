"""Заданы две клетки шахматной доски.
Если они покрашены в один цвет,
то выведите слово YES,
 а если в разные цвета – то NO."""

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")
