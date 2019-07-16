"""Дан список чисел. Выведите значение
 наибольшего элемента в списке,
 а затем индекс этого элемента в списке.
  Если наибольших элементов несколько,
выведите индекс первого из них."""

numList = list(map(int, input().split()))


def findBiggest(List: list):
    j = 0
    k = 0
    for x in range(len(List)):
        if (List[x] > j):
            j = List[x]
            k = x
    print(j, k)


findBiggest(numList)
