print('Wats is your name?')
your_name = input()
print('Wats is your birth year')
your_birth_year = int(input())
your_age = 2023 - your_birth_year
print('Your age:  ', (your_age))
def main():
    value = 5
    show_double(value)

# Функция show_double принимает аргумент
# и показывает его удвоенное значение.
def show_double(number):
    result = number * 2
    print(result)

# Вызвать функцию main.
main()