my_list = [-5, 19, 8, 1, 12, 14, 0, 3, -6, -19, 17, 7, 1, 5, -4, 10, -11, 9]

res = [i for i in my_list if i % 3 == 0 and i > 0 and i % 4 != 0]
print(res)
