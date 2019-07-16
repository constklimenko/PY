"""В олимпиаде по информатике принимало'
 участие несколько человек.

Определите и выведите средние баллы
участников олимпиады в 9 классе,
в 10 классе, в 11 классе.

Входные данные

Информация о результатах олимпиады записана
 в файле, каждая строка которого имеет вид:

фамилия имя класс балл.

Фамилия и имя — текстовые строки, не содержащие
пробелов. Класс - одно из трех чисел 9, 10, 11.
 Балл - целое число от 0 до 100.

В этой задаче файл необходимо считывать
 построчно, не сохраняя содержимое файла в памяти целиком.

Выходные данные

Выведите три числа: средние баллы по 9 классу,
 по 10 классу, по 11 классу. Входной файл в
  кодировке utf-8 (используйте open('input.txt',
   'r', encoding='utf-8'))."""

file = open("input.txt", encoding="utf8")

class9 = []
class10 = []
class11 = []
c = []

for line in file:
    # print(line)

    if int(line.split()[2]) == 9:
        # print(line.split())
        class9.append(list(line.split())[3])
        # print(class9)
    elif int(line.split()[2]) == 10:
        # print(line.split())
        class10.append(list(line.split())[3])
        # print(class10)
    elif int(line.split()[2]) == 11:
        # print(line.split())
        class11.append(list(line.split())[3])
        # print(class11)


def srednee(a):
    if len(a) == 0:
        return - 1
    summa = 0
    for x in a:
        summa += int(x)
    return summa / len(a)


c.append(srednee(class9))
c.append(srednee(class10))
c.append(srednee(class11))

print(" ".join(map(str, c)))
