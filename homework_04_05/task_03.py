# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you"
# и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

j = -1
for i in range(0, 101):
    j = j + 1
    print(j)
    answer = input('Should we break?')
    while answer != 'no' and answer != 'yes':
        answer = input('Dont understand you')
    if answer == 'yes':
        break