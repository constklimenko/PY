"""Выведите все элементы списка с
четными индексами (то есть A[0], A[2], A[4], ...). Программа
 должна быть эффективной и не выполнять лишних действий!"""

NumList = list(map(int, input().split()))
NumList2 = []

for x in range(0, len(NumList), 2):
    NumList2.append(NumList[x])

print(" ".join(map(str, NumList2)))
