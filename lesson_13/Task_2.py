import re
#"+375 (29) 123-45-67"
def is_phone_number(string: str) -> bool:
    # return re.fullmatch(r'\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}', string) is not None
    return re.fullmatch(r'[(29)], [(25)], [(44)]', string) is not None


if __name__ == '__main__':
    assert is_phone_number('+375 (29) 123-45-67')
    assert is_phone_number('555TR-9') == False
    assert is_phone_number('+375(29)123-45-67') == False
    assert is_phone_number('375 (29) 123-45-67') == False