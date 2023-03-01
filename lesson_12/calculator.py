def input_int_number() -> int:
    while True:
        try:
            number = int(input('Введите целон число: '))
            return number
        except ValueError as e:
            print('Ошибка:', e)
            print('Пробуйте снова: ')


class CalculationExitException(Exception):
    pass


def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '!':
        raise CalculationExitException()
    else:
        raise ValueError(f'Неподдерживаемая операция: {operation}')


def main():
    while True:
        left = input_int_number()
        right = input_int_number()
        operation = input('Введите операцию (введите ! для выхода из программы)')
        try:
            result = calculate(left, right, operation)
            print(result)
        except CalculationExitException:
            print('Завершаем программу')
            break
        except Exception as e:
            print(e)



if __name__ == '__main__':
    main()
