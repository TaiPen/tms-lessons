# Программа загадывает случайное число от 0 до 10.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в в какую сторону идти.
# То есть, если число пользователя слишком большое - выведите “не угадал, ваше число больше загаданного”.
# Если меньше - выведите “не угадал, ваше число меньше загаданного”.

import random
n = random.randint(1, 10)
while True:
    j = int(input('Enter a number: '))
    if j == n:
        print('Congrats!')
        break
    if j > n:
        print('не угадал, ваше число больше загаданного')
    if j < n:
        print('не угадал, ваше число меньше загаданного')