# Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка.

a = []
def list_sum (a):
    summa = 0
    for i in a:
        summa = summa + i
    return summa


a = [1, 2, 3]
print(list_sum(a))

print(list_sum([100, 200]))