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
            first_sub = str(input('Введите Имя '))
            last_sub = str(input('Введите Фамилию '))
            numb_sub = str(input('Введите номер телефона '))
            date_sub = (first_sub, last_sub, numb_sub)
            with sqlite3.connect('Phone_b.db') as connection:
                connection.execute('''INSERT INTO book (first_name, last_name, phone_number)
                                            VALUES (?,?,?)''', date_sub)
        elif num == 2:
            print('2. Список контактов в алфавитном порядке: ')
            with sqlite3.connect('Phone_b.db') as connection:
                books = connection.execute('SELECT * from book ORDER BY last_name')
                for el in books.fetchall():
                    print(el)
        elif num == 3:
            print('3. Обновите номер контакта: ')
            last_sub = str(input('Введите Фамилию '))
            numb_sub = str(input('Введите НОВЫЙ номер телефона '))
            upd_sub = (numb_sub, last_sub)
            with sqlite3.connect('Phone_b.db') as connection:
                connection.execute('''UPDATE book 
                                    SET phone_number = ?
                                    WHERE last_name == ?''', upd_sub)


phonebook()