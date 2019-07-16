"""Аня и Боря любят играть в разноцветные кубики,
 причем у каждого из них свой набор и в каждом
 наборе все кубики различны по цвету.
 Однажды дети заинтересовались, сколько существуют
  цветов таких, что кубики каждого цвета присутствуют
  в обоих наборах. Для этого они занумеровали все
   цвета случайными числами. На этом их энтузиазм иссяк,
    поэтому вам предлагается помочь им в оставшейся части.
     Номер любого цвета — это целое число в пределах
      от 0 до 10⁹."""

myList = list(map(int, input().split()))
n = myList[0]
m = myList[1]

anya = set()
borya = set()

for _ in range(n):
    anya.add(int(input()))

for _ in range(m):
    borya.add(int(input()))

a = anya & borya
b = anya - borya
c = borya - anya
f = open("output.txt", "w", encoding="utf8")

# print(len(a))
#
# print(*sorted(a))
#
# print(len(b))
#
# print(*sorted(b))
#
# print(len(c))
#
# print(*sorted(c))

# f.writelines(len(a), *sorted(a), len(b), *sorted(b), len(c), *sorted(c))
