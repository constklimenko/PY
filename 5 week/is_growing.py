"""Дан список. Определите, является ли он
 монотонно возрастающим(то есть верно ли,
 что каждый элемент этого списка больше
  предыдущего).Выведите YES,
   если массив монотонно возрастает и NO
    в противном случае.Решение оформите в
    виде функции IsAscending(A).В данной
    функции должен быть один цикл while, не
     содержащий вложенных условий и циклов
      — используйте схему линейного поиска."""


def IsAscending(A):
    asc = True
    x0 = 0
    x = 1
    while x < len(A):
        asc = (A[x] > A[x0])
        x0 += 1
        x += 1
    return asc


NumList = list(map(int, input().split()))
if IsAscending(NumList):
    print('YES')
else:
    print('NO')
