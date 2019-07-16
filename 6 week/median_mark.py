"""Для поступления в вуз абитуриент
 должен предъявить результаты трех
 экзаменов в виде ЕГЭ, каждый из них
 оценивается целым числом от 0 до 100 баллов.
  При этом абитуриенты, набравшие менее 40
   баллов (неудовлетворительную оценку)
   по любому экзамену из конкурса выбывают.
    Остальные абитуриенты участвуют в
     конкурсе по сумме баллов за три экзамена.

В конкурсе участвует N человек,
при этом количество мест равно K.
Определите проходной балл, то есть
 такое количество баллов, что количество
  участников, набравших столько или
  больше баллов не превосходит K,
  а при добавлении к ним абитуриентов,
  набравших наибольшее количество баллов
  среди непринятых абитуриентов, общее
  число принятых абитуриентов станет больше K.

Формат ввода

Программа получает
на вход количество мест K. Далее идут
 строки с информацией об абитуриентах,
 каждая из которых состоит из имени
 (текстовая строка содержащая произвольное
  число пробелов) и трех чисел от 0 до 100,
   разделенных пробелами.

Используйте для ввода файл input.txt
с указанием кодировки utf8 (для создания
 такого файла на своем компьютере в программе
 Notepad++ следует использовать кодировку UTF-8 без BOM).

Формат вывода

Программа должна вывести проходной балл в конкурсе.
Выведенное значение должно быть минимальным баллом,
который набрал абитуриент, прошедший по конкурсу.

Также возможны две ситуации, когда проходной
балл не определен.

Если будут зачислены все абитуриенты,
 не имеющие неудовлетворительных оценок,
 программа должна вывести число 0.

Если количество имеющих равный
максимальный балл абитуриентов больше чем K,
программа должна вывести число 1.

Используйте для вывода файл output.txt
с указанием кодировки utf8.

"""

file = open("input.txt", "r", encoding="utf8")

studentList2 = file.readlines()

k = int(studentList2.pop(0))
stList = [0] * len(studentList2)

for x in range(len(studentList2)):
    stList[x] = list(map(int, studentList2[x].split()[-1:-4:-1]))

# for x in range(len(stList)):
#     for y in stList[x]:
#         y = int(y)
# print(len(stList))
# print(type(stList[1][1]))
# print(len(stList))
# blackList = []
studentList2.clear()

for x in range(len(stList)):
    if (stList[x][0] >= 40 and stList[x][1] >= 40 and stList[x][2] >= 40):
        # print(stList[x])
        studentList2.append(stList[x][0] + stList[x][1] + stList[x][2])
    else:
        continue
    # print(studentList2)
#     # добавляем в черный список номера двоечников
#     # print(x)
#     # print(stList)
#     for y in range(0, 3):
#         # print(stList[x][y])
#         if stList[x][y] < 40:
#             blackList.append(x)
#         # print(stList)
#
# studentList.clear()
# # добавляем всех не-двоечников в новый список
# for x in range(len(stList)):
#     if x not in blackList:
#         studentList.append(stList[x])


# print(studentList)

# for x in range(len(studentList)):
#     studentList2[x] = (studentList[x][0] +
#                           studentList[x][1]
#                                    + studentList[x][2])

studentList2.sort(reverse=True)
stList.clear()
# print(studentList2)


oldMaxMark = studentList2[0]
maxMark = studentList2[0]

for x in range(k):
    if x < len(studentList2):
        stList.append(studentList2[x])
        if studentList2[x] < maxMark:
            oldMaxMark = maxMark
            maxMark = studentList2[x]
    else:
        break


# # print(len(studentList2))
#
if k < len(studentList2):
    if stList[k - 1] == studentList2[k]:
        if stList[k - 1] == stList[0]:
            print(1)
        else:
            print(oldMaxMark)
    else:
        print(maxMark)
#
#
elif k >= len(studentList2):
    print(0)
