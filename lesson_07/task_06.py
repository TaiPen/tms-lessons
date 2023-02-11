# Дан список чисел. Увеличьте каждый элемент в 100 раз.

def input_list():
    return [int(num) for num in input().split()]


my_list = input_list()
print(list(map(lambda x: x * 100, my_list)))

# Дан список чисел. Преобразуйте этот список в список строк.
print(list(map(lambda x: str(x), my_list)))
print(list(map(str, my_list)))


# Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).
print(list(map(lambda x: round((x / 100), 1), my_list)))

# * Напишите свою реализацию функций my_map, возвращающую список.
def my_map(func: iterable) -> list:
    return [func(el) for el in iterable]

print(list(map(lambda list(x), my_list)))