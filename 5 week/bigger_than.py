"""Дан список чисел. Выведите все элементы списка,
 которые больше предыдущего элемента.

"""

NumList = list(map(int, input().split()))

Bigger = []
previouse = NumList[0]

for x in range(1, len(NumList)):
    if NumList[x] > previouse:
        Bigger.append(NumList[x])
    else:
        pass
    previouse = NumList[x]

#print(" ".join(map(str, Bigger)))
print(*Bigger)