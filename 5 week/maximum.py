"""Найдите наибольшее значение в списке
и индекс последнего элемента, который
 имеет данное значение за один проход по списку,
 не модифицируя
этот список и не используя дополнительного списка."""

NumList = list(map(int, input().split()))
max1 = 0
num = 0

for x in range(len(NumList)):
    if NumList[x] >= max1:
        max1 = NumList[x]
        num = x

print(max1, num)
