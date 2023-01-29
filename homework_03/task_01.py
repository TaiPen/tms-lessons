# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.

side = float(input())
perimeter = side * 4
square = side * side
diagonal = side * (2**0.5)
tuple_sq = (perimeter, square, diagonal)
print(tuple_sq)