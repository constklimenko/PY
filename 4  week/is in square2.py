def IsPointInSquare(x, y):
    return (abs(x) <= 1 and abs(y) <= 1) and abs(y) <= 1 - abs(x)

x = float(input())
y = float(input())

if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
