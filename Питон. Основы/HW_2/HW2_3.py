my_list = [2, 5, 12, 8, 2, 12, 2, 2]
res = []
for val in my_list:
    if my_list.count(val) == 1:
        res.append(val)
print(res)
