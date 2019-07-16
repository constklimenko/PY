"""Есть две коробки, первая размером A₁×B₁×C₁,
вторая размером A₂×B₂×C₂. Определите,
можно ли разместить одну из этих коробок внутри другой,
при условии, что поворачивать коробки
можно только на 90 градусов вокруг ребер."""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if d > e:
    [d, e] = [e, d]
if d > f:
    [d, f] = [f, d]
if d > e:
    [d, e] = [e, d]
if e > f:
    [e, f] = [f, e]

if a > b:
    [a, b] = [b, a]

if a > c:
    [a, c] = [c, a]

if a > b:
    [a, b] = [b, a]

if b > c:
    [b, c] = [c, b]


if (a == d and b == e) and c == f:
    print("Boxes are equal")
elif ((a >= d and b >= e) and c >= f):
    print("The first box is larger than the second one")
elif ((a <= d and b <= e) and c <= f):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
