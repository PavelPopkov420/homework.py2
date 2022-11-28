# Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
import random

max = 0
max2 = 0

a = int(input('Введите значение А: '))
for i in range(a):
    b = random.randint(0, 99)
    print(b)
    if b > max:
        max = b
        continue
    elif max2 < b < max:
        max2 = b
print(f'Максимальное значение: {max}')
print(f'Второе максимальное значение: {max2}')