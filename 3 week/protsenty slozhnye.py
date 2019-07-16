

pr = int(input())
rub = int(input())
kop = int(input())
year = int(input())


def f(pr, rub, kop):
    sum = rub * 100 + kop

    sum = int((sum * (100 + pr)) / 100)

    rub = sum // 100

    kop = sum % 100

    return [rub, kop]

i = 0
while i < year:
    a = f(pr, rub, kop)
    rub = a[0]
    kop = a[1]
    i += 1

print(rub, kop)
