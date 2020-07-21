# Использование команды break

name = None
while name != 'Guido':
    name = input('Кто создатель Python? Ваш ответ: ')
    if name == 'Guido':
        break
    print('НЕ Верно!')
print('Совершенно верно!')

# Поскольку предусмотрен выход из цикла с помощью break, можно применить while True.
name = None
while True:
    name = input('Кто создатель Python? Ваш ответ: ')
    if name == 'Guido':
        break
    print('НЕ Верно!')
print('Совершенно верно!')