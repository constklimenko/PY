"""В списке все элементы попарно различны.
 Поменяйте местами минимальный
 и максимальный элемент этого списка."""

NumList = list(map(int, input().split()))
max1 = 0
min1 = NumList[0]
num = 0
numMax = 0
numMin = 0

for x in range(len(NumList)):
    if NumList[x] >= max1:
        max1 = NumList[x]
        numMax = x

for x in range(len(NumList)):
    if NumList[x] <= min1:
        min1 = NumList[x]
        numMin = x

NumList[numMax] = min1
NumList[numMin] = max1

print(" ".join(map(str, NumList)))
