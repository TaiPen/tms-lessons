# Напишите функцию input_list, которая не принимает входных аргументов, в просто читает строку,
# которую ввёл пользователь (вызывая функцию input), разбивает её по пробелам (с помощью функции split),
# и возвращает список целых чисел.

def input_list ():
    return [int(num) for num in input().split()]


def input_list ():
    return list(map(int, input().split()))