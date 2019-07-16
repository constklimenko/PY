file = open("input.txt", "r", encoding="utf8").readlines()

# wordList = list(map(str, file.split()))

wordDict = {}
wordList = []


for line in file:
    wordList += list(map(str, line.split()))

for x in range(len(wordList)):
    if wordDict.get(wordList[x], 0):
        # print(wordDict[wordList[x]], end=" ")
        wordDict[wordList[x]] += 1
    else:
        # print("0", end=" ")
        wordDict[wordList[x]] = 1

tupleList = []
i = iter(wordDict.items())

for x in range(len(wordDict)):
    a = next(i)
    tupleList.append((a[1], a[0]))

# s = lambda f: -int(f[0]), f[1]

b = sorted(tupleList, key=lambda x: x[0], reverse=True)

number = b[0][0]
helpList = []

for x in range(len(b)):
    if b[x][0] == number:
        helpList.append(b[x][1])
        # print(helpList)
    else:
        helpList.sort()
        for i in helpList:
            print(i)
        helpList.clear()
        helpList.append(b[x][1])
        number = b[x][0]

helpList.sort()
for i in helpList:
    print(i)
# print(sorted(tupleList))
