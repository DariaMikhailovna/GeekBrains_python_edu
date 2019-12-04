name = input('Введите имя: ')
surname = input('Введите Фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))

if age > 40 and (50 > weight or weight > 120):
    print('Следует обратиться к врачу!')
elif age <= 30 and 50 <= weight <= 120:
    print('Хорошее состояние')
elif age > 30 and (50 > weight or weight > 120):
    print('Следует заняться собой')
elif age <= 30 and (50 > weight or weight > 120):
    print('Всё плохо')
else:
    print('Всё нормально')