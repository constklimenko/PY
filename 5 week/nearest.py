"""Напишите программу, которая находит в массиве элемент,
самый близкий по величине к данному числу."""

sizeOfArray = int(input())
Array = list(map(int, input().split()))
number = int(input())

radius = 2001
answer = 0

for x in Array:
    if abs(x - number) < radius:
        radius = abs(x - number)
        answer = x

print(answer)
