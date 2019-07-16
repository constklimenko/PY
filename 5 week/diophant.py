"""Даны числа a, b, c, d, e.
Подсчитайте количество таких целых
чисел от 0 до 1000, которые являются корнями
уравнения (ax³+bx²+cx+d)/(x-e)=0,
и выведите их количество."""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

num = 0
for x in range(1001):
    if x != e:
        if (a * x**3 + b * x**2 + c * x + d) / (x - e):
            num += 1 
print(num)
