numList = list(map(int, input().split()))

k = int(input())

for x in range(k,len(numList) - 1):
    numList[x], numList[x + 1] = numList[x + 1], numList[x]

numList.pop()
print(" ".join(map(str,numList)))
