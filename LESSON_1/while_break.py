# while-else
# В блоке else (после while) выполняем действие после того как вышли из цикла while
# когда условие цикла стало неверным (False).

number = 0
while number <= 100:
    print(number)
    number += 1
    if number == 33:
        break
else:
    print('else - end')
print('End')