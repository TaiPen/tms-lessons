second = int(input('Insert seconds: '))
minutes = int(second // 60)
hours = int(second // 360)
days = int(second // 2400)
print(days, hours, minutes)