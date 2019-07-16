"""Каждый из N школьников некоторой школы
 знает Mᵢ языков. Определите, какие языки
  знают все школьники и языки, которые
  знаетхотя бы один из школьников.

Формат ввода

Первая строка входных данных содержит
количество школьников N. Далее идет N чисел Mᵢ,
 после каждого из чисел идет Mᵢ строк, содержащих
 названия языков, которыезнает i-й школьник.
  Длина названий языков не превышает 1000 символов,
   количестворазличных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.

Формат вывода

В первой строке выведите количество языков,
 которые знают все школьники. Начиная со
 второй строки - список таких языков. Затем
 - количество языков, которые знает хотя бы
  один школьник, на следующих строках -
   список таких языков."""

n = int(input())

unicLang = set()

wideLang = set()
trigger = True

for i in range(n):
    m = int(input())
    mSet = set()
    for j in range(m):
        s = input()
        unicLang.add(s)
        mSet.add(s)

    if bool(wideLang):
        wideLang &= mSet
    elif trigger:
        wideLang = mSet
        trigger = False

# print("wide= ", wideLang)
# print("unic= ", unicLang)

print(len(wideLang))
w = iter(wideLang)
for _ in range(len(wideLang)):
    print(next(w))

print(len(unicLang))
u = iter(unicLang)
for _ in range(len(unicLang)):
    print(next(u))
