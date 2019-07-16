"""Известно, что фамилии всех участников — различны.
 Сохраните в массивах список всех участников
  и выведите его, отсортировав по фамилии
  в лексикографическом порядке.
  При выводе указываете фамилию, имя участника и его балл.

Используйте для ввода и вывода файлы input.txt
и output.txt с указанием кодировки utf8.
 Например, для чтения откройте файл с помощью open('input.txt',
  'r', encoding='utf8').

Входные данные:

Строки вида "Фамилия Имя НомерШколы Балл"."""

file = open("input.txt", "r", encoding="utf8")
outfile = open("output.txt", "w", encoding="utf8")
a = file.readlines()
a.sort()
b = []
for x in a:
    c = x.split()
    c = [c[0], c[1], c[3]]
    b.append(" ".join(c) + "\n")
outfile.writelines(b)
