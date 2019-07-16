"""За многие годы заточения узник замка Иф
проделал в стене прямоугольное отверстие
размером D×E. Замок Иф сложен из кирпичей,
 размером A×B×C.
 Определите, сможет ли узник выбрасывать
  кирпичи в море через это отверстие,
  если стороны кирпича должны быть
   параллельны сторонам отверстия."""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if d > e:
    [d, e] = [e, d]

if a > b:
    [a, b] = [b, a]

if a > c:
    [a, c] = [c, a]

if a > b:
    [a, b] = [b, a]

if b > c:
    [b, c] = [c, b]

if a <= d and b <= e:
    print("YES")
else:
    print("NO")
