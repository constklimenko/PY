"""Найдите и выведите все двузначные числа,
 которые равны удвоенному произведению своих цифр.
"""

for x in range(10, 100):
    n = x // 10
    m = x % 10
    if x == n * m * 2:
        print(x)
