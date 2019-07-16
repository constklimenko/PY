"""В выборах Президента Российской Федерации
побеждает кандидат, набравший свыше половины
числа голосов избирателей. Если такого кандидата нет,
 то во второй тур выборов выходят два кандидата,
 набравших наибольшее число голосов.

Формат ввода

Каждая строка входного файла
 содержит имя кандидата, за которого отдал
  голос один избиратель. Известно, что общее
  число кандидатов не превосходит 20, но в отличии
   от предыдущих задач список кандидатов явно
   не задан. Читайте данные из файла input.txt
    с указанием кодировки utf8.

Формат вывода

Если есть кандидат,
набравший более 50% голосов,
программа должна вывести его имя.
 Если такого кандидата нет, программа
 должна вывести имя кандидата, занявшего
  первое место, затем имя кандидата, занявшего
   второе место. Выводите данные в файл output.txt
   с указанием кодировки utf8."""


def SumTuple(tuple1):
    summ = 0
    for _ in range(len(tuple1)):
        summ += tuple1[_][1]
    return summ


file = open("input.txt", "r", encoding="utf8")
outfile = open("output.txt", "w", encoding="utf8")


wordList = file.readlines()

# for x in a:
#     wordList += x

wordDict = {}

for x in range(len(wordList)):
    if wordDict.get(wordList[x], 0):
        # print(wordDict[wordList[x]], end=" ")
        wordDict[wordList[x]] += 1
    else:
        # print("0", end=" ")
        wordDict[wordList[x]] = 1

wordTuple = list(wordDict.items())
wordTuple.sort(key=lambda x: x[1], reverse=True)

# print(wordTuple)

if wordTuple[0][1] > SumTuple(wordTuple)/2:
    # print(wordTuple[0][0])
    outfile.writelines(wordTuple[0][0])
else:
    # print(wordTuple[0][0], end='')
    # print(wordTuple[1][0])
    outfile.writelines([wordTuple[0][0], wordTuple[1][0]])
