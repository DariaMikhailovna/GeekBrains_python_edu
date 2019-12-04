my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
res = []
for item in my_list_1:
    if item not in my_list_2:
        res.append(item)
print(res)