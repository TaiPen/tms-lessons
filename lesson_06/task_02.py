# 1. Посчитайте сумму чисел от 1 до 10. (ответ: 55)
summa = 0
for i in range (1, 11):
    summa = summa + i
print(summa)


# 2. Дан список чисел. Найти их сумму.
a = (10, 15, 6)
summa = 0
for i in a:
    summa = summa +i
print(summa)


# 3. Дан список чисел. Найти их максимальное среди них.
a = [10, 15, 6, -9]
b = a[]
for i in  a:
    if i > b:
        b = i
print(b)


# 4. Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.
a = [10, 15, 6, 0, -9]
for i in a:
    if i == 0:
        print('yes')
        break
    else:
        print('no')
