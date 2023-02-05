# Напишите функцию get_natural_numbers, которое принимает целое число n
# и возвращает список натуральных чисел от 1 до n включительно. Используйте генераторы списков.
def get_natural_numbers(numb: int):
    numbers = []
    for i in range(1, numb + 1):
        numbers.append(i)
    return numbers


print(get_natural_numbers(3))
print(get_natural_numbers(11))