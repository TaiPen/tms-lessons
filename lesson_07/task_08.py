from functools import reduce

# Дан список чисел. Найти его сумму.
my_list = [1, 2, 3, 4]
print(reduce((lambda a, b: a + b, my_list)))

# Дан список чисел. Найти минимальное число.
print(min(my_list))
print(reduce(lambda a, b: min(a, b), my_list, 0))

# Дан список чисел. Найти произведение всех элементов.
print(reduce(lambda a, b: a * b, my_list))

# * Напишите свою реализацию функции my_reduce. Для простоты можно сделать третий параметр обязательным.
def my_reduce (func, iterable, initial_value):
    result = initial_value
    for el in iterable: