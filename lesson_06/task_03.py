# 1. Напишите функцию hello_world, которая выводит строку 'Hello world!'. Вызовите эту функцию трижды.
def hello_world (set_word: str):
    return (set_word)


print(hello_world('Hello world!'))
print(hello_world('Hello world!'))
print(hello_world('Hello world!'))


# 2. Напишите функцию my_sum, которая принимает два числа и возвращает их сумму. Проверьте корректность её работы
# при разных значениях аргументов. Например my_sum(1, 2), my_sum(25, 75) и т.д.
def my_sum (numb1: float, numb2: float):
    return numb1 + numb2


print(my_sum(8, 26))
print(my_sum(30, -226))


# 3. Напишите функцию simple_compare, которая принимает два числа и возвращает True, если первое число меньше второго.
# Иначе возвращает False.
def simple_compare (numb1: float, numb2: float):
    if numb1 < numb2:
        return True
    else:
        return False


print(simple_compare(89, 105))
print(simple_compare(369, 105))


# 4. Напишите функцию compare, которая принимает два числа и возвращает -1 если первое число меньше второго,
# 1 если первое больше второго, и 0 если они равны. Примеры:
# compare(100, 200) -> -1
# compare(200, 100) -> 1
# compare(10, 10) -> 0
def compare (numb1: float, numb2: float) -> float:
    if numb1 < numb2:
        return (-1)
    elif numb1 > numb2:
        return (1)
    else:
        return (0)


print(compare(8, 10))
print(compare(108, 10))
print(compare(10, 10))


# 5. Напишите функцию filter_negative_numbers, которая принимает список чисел, и возвращает новый список,
# составленный из элементов первого без отрицательных чисел, Пример:
# filter_negative_numbers([6, -5, 0, -1, 100]) -> [5, 0, 100]
def filter_negative_numbers (numb_list: list):
    for i in numb_list:
        if i < 0:
            numb_list.remove(i)
    return numb_list


print(filter_negative_numbers([2, 36, -5, 25, -4]))