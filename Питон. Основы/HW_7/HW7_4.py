def my_func(number):
    if number < 1 or number > 100:
        raise ValueError('Число должно быть от 1 до 100')
    if number == 13:
        raise ValueError('Вы ввели число 13')
    else:
        return number ** 2


numb = int(input('Введите число от 1 до 100: '))
try:
    res = my_func(numb)
except ValueError as er:
    print(er)
else:
    print(res)
