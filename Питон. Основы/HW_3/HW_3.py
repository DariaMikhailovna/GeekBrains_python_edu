import random

left = 1
right = 100
print('Загадайте число от 1 до 100!')
while True:
    number = random.randint(left, right)
    print(f'Это число {number}?')
    answer = input('Введите ответ символами > (если загаданное число больше), < (если меньше), = (угадал): ')
    if answer == '=':
        print('Ура! Победа!')
        break
    elif answer == '>':
        left = number + 1
    elif answer == '<':
        right = number - 1


