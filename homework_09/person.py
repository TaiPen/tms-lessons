class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f"Person: {self.full_name} ({self.gender}), {self.age} years old")

    def get_birth_year(self):
        birth_year = 2023 - self.age
        return birth_year

my_person = Person('Dzmitry', 36, 'M')

my_person.print_person_info()
print(my_person.age)
print(my_person.full_name)
print(my_person.gender)
print(my_person.get_birth_year())
