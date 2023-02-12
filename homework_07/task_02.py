# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
#
# Пример:
# Ввод пользователя: a b c d e f o
# Результат программы: ['b', 'c', 'd', 'f']
str_letter = input('Введите латинские буквы через пробел: ').split()
def remove_vowels (str_letter : list):
    for el in str_letter[::-1]:
        if el in 'a, e, i, o, u':
            str_letter.remove(el)
    return str_letter


print(remove_vowels(str_letter))

# Используя функцию filter():
str_letter = input('Введите латинские буквы через пробел: ')
def remove_vowels(str_letter : str):
    return str_letter.split()


filtered_str = list((filter(lambda el: el not in 'a, e, i, o, u', str_letter)))
print(filtered_str)
