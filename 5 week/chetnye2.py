NumList = list(map(int, input().split()))
NumList2 = []

for x in range(len(NumList)):
    if NumList[x] % 2 == 0:
        NumList2.append(NumList[x])

print(" ".join(map(str, NumList2)))
