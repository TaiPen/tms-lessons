import re


def is_car_number(string: str):
    return re.fullmatch(r'\d{4}\w{2}-\d', string) is not None

if __name__ == '__main__':
    assert is_car_number('5555TR-9')
    assert is_car_number('555TR-9') == False
    assert is_car_number('55555TR-9') == False
    assert is_car_number('5555TR 9') == False
