"""Дана последовательность натуральных чисел,
завершающаяся числом 0. Определите,какое наибольшее число
 подряд идущих элементов этой
 последовательности равны друг другу.

"""

x = int(input())
y = 0
s = 0
i = 1

while x != 0:
    if x != y:
        i = 1
    else:
        i += 1
    y = x
    if s < i:
        s = i
    x = int(input())
print(s)
