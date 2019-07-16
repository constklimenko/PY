"""Выведите элементы данного списка
в обратном порядке, не изменяя сам список."""

numList = list(map(int, input().split()))

print(" ".join(map(str, numList[::-1])))
