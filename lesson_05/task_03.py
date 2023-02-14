# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.
# Использовать встроенные sum и max разрешено.

def func_any(*args):
    summ_any = sum(list(*args))
    max_any = max(list(*args))
    print(max_any)
    print(summ_any)


func_any(897)