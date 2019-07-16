"""
Во входном файле (вы можете читать данные
из файла input.txt) записан текст. Словом
 считается последовательность непробельных
  подряд идущих символов. Слова разделены одним
  или большим числом пробелов или символами конца
   строки. Для каждого слова из этого текста подсчитайте,
сколько раз оно встречалось в этом тексте ранее.
"""

file = open("input.txt", "r", encoding="utf8")

a = file.readlines()
wordList = []

for x in a:
    wordList += x.split()

wordDict = {}

for x in range(len(wordList)):
    if wordDict.get(wordList[x], 0):
        print(wordDict[wordList[x]], end=" ")
        wordDict[wordList[x]] += 1
    else:
        print("0", end=" ")
        wordDict[wordList[x]] = 1


# print(wordList)
