# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
# в которой все слова из списка соединены через символ разделитель.
# # Пример ввода пользователя:
# hello this is my string
# @
# # Вывод программы: hello@this@is@my@string
# # Используйте функцию reduce.
from functools import reduce
str_letter = input('Введите латинские слова через пробел: ').split()
sep = input('Введите символ-разделитель: ')
def my_join():
    for el in str_letter:
        return [(el + sep) for el in str_letter]


new_letter = my_join()
print(reduce(lambda a, b: a + b, new_letter))