NumList = list(map(int, input().split()))
count = 0

for x in range(len(NumList)):
    if NumList[x] > 0:
        count += 1

print(count)
