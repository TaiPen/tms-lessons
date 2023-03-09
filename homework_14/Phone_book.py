import sqlite3


def phonebook():
    while True:
        print('0. Выйти из программы')
        print('1. Добавить новый контакт')
        print('2. Вывести весь список контактов в алфавитном порядке')
        print('3. Обновить номер контакта')
        num = int(input())
        if num == 0:
            print('Hasta la vista, baby!')
            break
        elif num == 1:
            print('1. Добавте новый контакт: ')
            with sqlite3.connect('Phone_b.db') as connection:


        elif num == 2:
