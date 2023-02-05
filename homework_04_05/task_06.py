# Напишите функцию is_year_leap, которая принимает число (год)
# и возвращает True если год високосный (см. комментарий к слайда), False если нет.

def is_year_leap (year: int) -> bool:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print(is_year_leap(1998))
print(is_year_leap(2000))
print(is_year_leap(2024))