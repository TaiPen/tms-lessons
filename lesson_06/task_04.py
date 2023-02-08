# Скопируйте функции прошлых 5 заданий в один файл.
# Напишите программу, спрашивает у пользователя номер задачи, решение которой он хочет проверить,
# пользователь вводит число от 1 до 5, в зависимости от выбранного номера запросите у пользователя входные данные
# для задачи (если это нужно) и выведите ответ. Примеры работы программы приведены в комментариях к слайду.
def hello_world():
    print('Hello World')


def my_sum(numb1: float, numb2: float):
    return numb1 + numb2


def simple_compare (numb1: float, numb2: float):
    if numb1 < numb2:       # return a < b
        return True
    else:
        return False


def compare(numb1: float, numb2: float) -> float:
    if numb1 < numb2:
        return (-1)
    elif numb1 > numb2:
        return (1)
    else:
        return (0)


def filter_negative_numbers(numb_list: list):
    for i in numb_list:
        if i < 0:
            numb_list.remove(i)
    return numb_list


def main_funcion(numb):
    if numb == 1:
        hello_world()
    elif numb == 2:
        numb1 = input('Введите первое число:')
        numb2 = input('Введите второе число:')
        print('Сумма чисел: ', my_sum())
    elif numb == 3:
        numb1 = input('Введите первое число:')
        numb2 = input('Введите второе число:')
        print('Первое число меньше второго? Ответ:',main_funcion())
    elif numb == 4:
        numb1 = input('Введите первое число:')
        numb2 = input('Введите второе число:')
        print('Результат сравнения:', compare())
    elif numb == 5:
        numb_list = input([])
        print('Мы удалили отрицательные числа из вашего списка:',filter_negative_numbers())
    else:
        print('Задачи с таким номером нет.')


main_funcion(int(input('Введите номер задачи:')))

