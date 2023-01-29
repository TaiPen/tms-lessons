# Пользователь вводит месяц и число. Выведите True, если такой день есть в году.

year = {'january': [29, 30, 31], 'february': 28, 'march': [29, 30, 31], 'april': [29, 30], 'may': [29, 30, 31],
        'june': [29, 30], 'july': [29, 30, 31], 'august': [29, 30, 31], 'september': [29, 30],
        'october': [29, 30, 31], 'november': [29, 30], 'december': [29, 30, 31]}
month = input()
date = int(input())
date_dict = year[month]
print(month in year and (date <= 28 or date in date_dict))