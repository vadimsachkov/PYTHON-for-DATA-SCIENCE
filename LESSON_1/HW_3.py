name = input("Input your name: ")
surname = input("Input your surname: ")
age = int(input("Input your age: "))
weight = int(input("Input your weight: "))
if age <= 30 and weight >= 50 and weight <= 120:
    print(name, surname, age, 'years,', 'weight', weight, 'kg', '- you are in good shape!')
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    print(name, surname, age, 'years,', 'weight', weight, 'kg', '- you need to take care of yourself!')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, surname, age, 'years,', 'weight', weight, 'kg', '- you need to see a doctor!')