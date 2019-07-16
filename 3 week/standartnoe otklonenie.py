from math import sqrt


ch = int(input())
a = []

while ch != 0:
    a.append(ch)
    ch = int(input())

d = 0

for i in a:
    d = i + d

s = d / len(a)

d2 = 0

for i in a:
    d2 = (i - s)**2 + d2

s = d2 / (len(a) - 1)

s = sqrt(s)


print(s)
