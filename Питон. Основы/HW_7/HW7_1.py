list_a = ['Киви', 'Апельсин', 'Банан', 'Ананас', 'Помидор']
list_b = ['Манго', 'Груша', 'Апельсин', 'Дыня', 'Киви', 'Арбуз']

res = [fruit for fruit in list_a if fruit in list_b]
print(res)
