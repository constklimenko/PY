"""Во входном файле (вы можете читать данные из sys.stdin,
 подключив библиотеку sys) записан текст.
  Словом считается последовательность непробельных
   символов идущих подряд, слова разделены одним
    или большим числом пробелов или символами конца
     строки. Определите, сколько различных слов
     содержится в этом тексте.

"""
mySet = set()

file = open("input.txt", "r", encoding="utf8").readlines()


for line in file:
    myList = list(line.split())
    # print(myList)
    for x in myList:
        mySet.add(x)

print(len(mySet))
