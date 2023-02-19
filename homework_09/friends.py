# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person. Добавьте в него некоторое количество
# вымышленных друзей с разными именами, возрастом и полом.
# Выведите информацию о каждом друге на экран.
# * Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# * Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter,
# либо генератор списков).
# * Заверните код из пунктов 5 и 6 в функции get_oldest_pearson и filter_male_person соответственно.

from person import Person
my_friends = [Person('Bruce Wayne', 40, 'M'),
              Person('Harley Quinn', 19, 'F'),
              Person('Clark Kent', 27, 'M')]


def get_oldest_pearson():
    winner = 0
    for el in my_friends:
        if el.age > winner.age:
            winner = el.age
    return winner


def filter_male_person():
    for el in my_friends:
        return list(filter(lambda person: person.gender == 'M', my_friends))

print(my_friends.get_oldest_pearson())
print(my_friends.filter_male_person())

# не работает, я сдаюсь :( :( :(