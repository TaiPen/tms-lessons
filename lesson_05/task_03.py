# Создать функцию sum_and_max, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них. Использовать встроенные sum и max разрешено.

def sum_and_max (*argx):
    return sum(argx), max(argx)


argx = 1, 2, 3
print(sum_and_max(*argx))