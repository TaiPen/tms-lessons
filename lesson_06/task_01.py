# 1. Даны два числа, если они равны выведите yes, иначе - no.
a = float(input())
b = float(input())
if a == b:
    print('yes')
else:
    print('no')


# 2. Даны два числа, вывести на экран максимальное из них.
a = float(input())
b = float(input())
if a > b:
    print(a)
else:
    print(b)

# 3. Дано число. Если оно положительно выведите yes, иначе no.
a = float(input())
if a > 0:
    print('yes')
else:
    print('no')


# 4. Дано число. Если оно положительно - выведите positive, если отрицательно - negative, если равно нулю - zero.
a = float(input())
if a > 0:
    print('positive')
elif a == 0:
    print('zero')
else:
    print('negative')


# 5. Даны три числа. Если они все больше 0 - вывести yes, иначе - no.
a = float(input())
b = float(input())
c = float(input())
if a > 0 and b > 0 and c > 0:
    print('yes')
else:
    print('no')


# 6. Дан номер месяца (число от 1 до 12). Выведите пору года, которой этот месяц принадлежит: зима, весна, лето или осень.
a = int(input())
if a == 1 or a == 2 or a == 12:
    print('зима')
elif a == 3 or a == 4 or a == 5:
    print('весна')
elif a == 6 or a == 7 or a == 8:
    print('лето')
else:
    print('осень')


# 7. Дано три числа. Вывести количество положительных чисел среди них.
