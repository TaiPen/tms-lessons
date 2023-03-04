# Напишите функцию is_float_number, которая принимает строку и возвращает bool.
# Функция должна вернуть True если переданная строка это корректное число с плавающей точкой. Например "1.0", "20.45".
import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'[-+]?\d+\.\d+', string) is not None


if __name__ == '__main__':
    assert is_float_number('1.0')
    assert is_float_number('-1.0')
    assert is_float_number('200.45')
    assert is_float_number('25') == False
    assert is_float_number('00000') == False
    assert is_float_number('2.5.78') == False
