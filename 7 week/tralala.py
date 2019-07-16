# file = input()
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

# print(wordDict)
tuple1 = list(wordDict.items())

# print(sorted(list(tuple1), key=lambda y:str(y[1]) + y[0]))
#
# print(sorted(tuple1, key=lambda y:y[1])[len(tuple1) - 1][0])

tuple1.sort(key=lambda y: y[1])

n = len(tuple1) - 1
List2 = []

# print(n)
# print(len(tuple1))

while tuple1[n][1] == tuple1[len(tuple1) - 1][1]:
    List2.append(tuple1[n][0])
    if n > 0:
        n -= 1
    else:
        break


print(sorted(List2)[0])
