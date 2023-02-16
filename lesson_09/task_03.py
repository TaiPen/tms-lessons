class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_voice(self):
        print(f'Я не знаю какой звук мне издать, я же абстрактное животное')


class Dog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    def make_voice(self):
        print(f'ГААААВ')

class Cat(Animal):
    def __init__(self, name, age, is_vaccinated):
        super().__init__(name, age)
        self.is_vaccinated = is_vaccinated

    def make_voice(self):
        print(f'This is SPAAAAAARTAAAA')


animals = [
   Animal('Животное', 5), # создание абстрактного животного довольно бессмысленно, но для понимания ООП это ок
   Dog('Шарик', 10, 'Доберман'),
   Cat('Матроскин', 9, True),
]
for animal in animals:
   animal.make_voice()
