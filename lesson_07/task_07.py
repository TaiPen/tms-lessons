# Дан список чисел. Удалите из него отрицательные числа.
my_list = [1, 2, 3, 4]
print(list(filter(lambda num: num >= 0, my_list)))

# Дан список чисел. Удалите из него нечётные числа.
print(list(filter(lambda num: num %2 == 0, my_list )))

# Дан список чисел. Выведите три числа: количество положительных чисел, поличество нулей,
# и количество отрицательных чисел. Используйте функции filter и len.
print(len(filter(lambda num: num > 0, my_list)))
print(len(filter(lambda num: num == 0, my_list)))


# * Напишите свою реализацию функций my_filter, возвращающую список.
def my_filtr(func: iterable):
    return [num for num ]

