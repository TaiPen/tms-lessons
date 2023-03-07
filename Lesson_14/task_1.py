import sqlite3


with sqlite3.connect('sqlite.db') as connection:
    users = connection.execute('SELECT * from user')
    for user in users.fetchall():
        print(user)

    min_age = int(input())
    connection.execute('SELECT * from user'
                       'where age >= ? '
                       'order by age', (min_age,))
    for user in users.fetchall():
        print(user)