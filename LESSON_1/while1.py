# 1. Вывод чисел от 0 до 100.
# 2. Вывод чисел от 0 до n.
# 3. Вывод четных чисел.

# 1. Вывод чисел от 0 до 100.
number = 0
while number <= 100:
    print(number)
    number += 1
    # number = number +1
print('*' * 30)

# 2. Вывод чисел от 0 до n от пользователя.
number = 0
n = int(input('Введите число: '))
while number <= n:
    print(number)
    number += 1
print('*' * 30)

# 3. Вывод четных чисел от 0 до n от пользователя.
number = 0
n = int(input('Введите число: '))
while number <= n:
    if number % 2 == 0:     # Если вместо 0 поставить 1 (либо знак != 0), выведутся нечетные числа.
        print(number)
    number += 1
print('*' * 30)