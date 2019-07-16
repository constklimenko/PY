"""Петя перешёл в другую школу.
На уроке физкультуры ему понадобилось
определить своё место в строю.
Помогите ему это сделать.

Формат ввода

Программа получает на вход невозрастающую
 последовательность натуральных чисел,
 означающих рост каждого человека в строю.
 После этого вводится число X – рост Пети.
 Все числа во входных данных натуральные и не превышают 200.

Формат вывода

Выведите номер, под которым Петя
должен встать в строй. Если в строю
есть люди с одинаковым ростом,таким же,
как у Пети, то он должен встать после них"""

numList = list(map(int, input().split()))
height = int(input())
n = 0

for x in range(len(numList)):
    if numList[x] >= height:
        n += 1

n += 1
print(n)
