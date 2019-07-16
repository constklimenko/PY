a = str(input())

i1 = a.find("h")
i2 = a.rfind("h")

b = a[0:i1 + 1] + 2 * a[i1 + 1:i2] + a[i2:len(a)]

print(b)
