import random as rnd


def get_rnd_item(items):
    if not items:
        return None
    else:
        return rnd.choice(items)


if __name__ == '__main__':
    print(get_rnd_item([1, 2, 3, 4]))
