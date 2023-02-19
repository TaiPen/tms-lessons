# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# * Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count

from student import Student
students = [Student('Bruce Wayne', 4.5),
            Student('Harley Quinn', 6.5),
            Student('Clark Kent', 9.2)]


def calc_sum_scholarship(self):
    sum_scholarship = 0
    for el in students:
        sum_scholarship += el.get_scholarship()
    return sum_scholarship


def get_excellent_student_count(self):
    excellent_count = 0
    for el in students:
        excellent_count += el.is_excellent()
    return excellent_count


print(students.calc_sum_scholarship())
print(students.get_excellent_student_count())

# не работает, я сдаюсь :( :( :(