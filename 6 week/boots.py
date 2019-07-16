"""В обувном магазине продается обувь разного размера.
 Известно, что одну пару обуви можно надеть на другую,
  если она хотя бы на три размера больше. В магазин
пришел покупатель.Требуется определить,
 какое наибольшее количество пар обуви сможет
 предложить ему продавец так, чтобы он смог
  надеть их все одновременно.

Формат ввода

Сначала вводится размер
 ноги покупателя (обувь
 меньшего размера он надеть не сможет),
  в следующей строке — размеры каждой пары обуви
   в магазине через пробел. Размер — натуральное
    число, не превосходящее 100."""

n = int(input())
NumList1 = list(map(int, input().split()))

NumList1.sort()

x = 0
ans = []

while NumList1[x] < n:
    x += 1
currentSize = NumList1[x]
ans.append(NumList1[x])

for y in range(x + 1, len(NumList1)):
    if NumList1[y] >= currentSize + 3:
        ans.append(NumList1[y])
        currentSize = NumList1[y]
    else:
        continue

print(len(ans))