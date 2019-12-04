import os


def add_dirs():
    for num in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{num}')
        os.mkdir(new_path)


if __name__ == '__main__':
    add_dirs()


def delete_dirs():
    for num in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{num}')
        os.rmdir(new_path)


if __name__ == '__main__':
    delete_dirs()
