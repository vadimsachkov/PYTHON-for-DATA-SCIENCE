# Использование команды continue (переход на следующую итерацию цикла.
# Команды в цикле после continue не выполняются)
# Вывод нечетных чисел от 0 до n.

number = 0
n = int(input('Enter n: '))
while number <= n:
    if number % 2 == 0:     # для вывода четных чисел ставим !=
        number += 1
        continue
    print(number)
    number += 1