# Пользователь вводит два числа: x, y, где x - сумма рублей, которую он кладёт на депозит под 10% годовых,
# y - количество лет. Каждый год вклад увеличивает на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты
# Вывести конечную сумму на счету по прошествии y лет.

start_money = float(input())
years = int(input())
end_money = float(start_money * ((1 + 0.1) ** years))
print(end_money)