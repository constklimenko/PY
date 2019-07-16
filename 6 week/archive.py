"""Системный администратор вспомнил,
 что давно не делал архива пользовательских файлов.
 Однако, объем диска, куда он может поместить архив,
  может быть меньше чем суммарный объем
   архивируемых файлов.

Известно, какой объем занимают файлы
каждого пользователя.

Напишите программу, которая
 по заданной информации о пользователях
 и свободному объему на архивном диске
  определит максимальное число пользователей,
  чьи данные можно поместить в архив.

Формат ввода

Программа получает на вход в одной строке число
 S – размер свободного места на диске
  (натуральное, не превышает 10000), и число
  N – количество пользователей (натуральное,
   не превышает 100), после этого идет N чисел
   - объем данных каждого пользователя (натуральное,
    не превышает 1000), записанных каждое в отдельной строке.

Формат вывода

Выведите наибольшее количество
пользователей, чьи данные могут
быть помешены в архив."""
b = list(map(int, input().split()))
S = b[0]
N = b[1]
a = [0] * N

for x in range(N):
    a[x] = int(input())

a.sort()

summa, i, j = 0, 0, 0

while (summa <= S) & (i < len(a)):
    """:"""
    summa += a[i]
    i += 1
    j += 1
    # print("summa=", summa, "j=", j)

if summa > S:
    j -= 1

print(j)