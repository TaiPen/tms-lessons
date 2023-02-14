sum = 0
for number in range (1, 101):
    sum += number
print(f' Task_1: {sum}')


sum = 0
for number in range (100, 1001):
    sum += number
print(f' Task_2: {sum}')


sum = 0
for number in range (100, 1001, 2):
    sum += number
print(f' Task_3: {sum}')


fact = 1
for num in range (2, 11):
    fact = fact * num
print(f' Task_4: {fact}')


sum = 1
for number in range (1, 11):
    sum = sum * 2
print(f' Task_5: {sum}')


sum = 0
i = 1
while sum <= 1000:
    sum = sum + 1
    i = i + 1
print(f' Task_6: {sum}')
