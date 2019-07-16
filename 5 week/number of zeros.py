"""Дано несколько чисел. Подсчитайте,
 сколько из них равны нулю,
и выведите это количество."""

n = int(input())
num = 0

for x in range(n):
    a = int(input())
    if a == 0:
        num += 1

print(num)
