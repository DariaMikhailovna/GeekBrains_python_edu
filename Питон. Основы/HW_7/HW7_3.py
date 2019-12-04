import math


def my_func(items):
    return [math.sqrt(item) if item > 0 else item for item in items]


my_list = [4, -7, 2, 8, -10, 16, 49, 0, 225]
print(my_func(my_list.copy()))
print(my_list)
