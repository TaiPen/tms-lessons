# * Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
# a m S I o E y H l v O E
str_letter = input('Введите латинские буквы через пробел: ').split()


def remove_vowels(str_letter : str):
    return list((filter(lambda el: el.lower() not in 'a, e, i, o, u', str_letter)))


print(remove_vowels(str_letter))