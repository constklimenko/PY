"""
+___ +___ +___
|1 / |2 / |3 /
|__\ |__\ |__\
|    |    |    """

n = int(input())

str1 = "+___ "*n
str2 = ""
for x in range(1, n + 1):
    str2 = str2 + "|" + str(x) + " / "
str3 = "|__\ "*n
str4 = "|    "*n

print(str1)
print(str2)
print(str3)
print(str4)
