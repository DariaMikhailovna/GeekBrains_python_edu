import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='UTF-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть!')


def get_list(folders_only=False):
    res = os.listdir()
    if folders_only:
        res = [item for item in res if os.path.isdir(item)]
    print(res)


def delete_file_or_folder(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print('Нет такого файла или папки!')


def copy_file_or_folder(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print(f'Невозможно создать файл, так как он уже существует: {new_name}')
    else:
        try:
            shutil.copyfile(name, new_name)
        except FileNotFoundError:
            print('Нет такого файла!')


def save_info(massage):
    current_time = datetime.datetime.now()
    res = f'{current_time} - {massage}'
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(res + '\n')


def change_current_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('Нет такой директории')
    else:
        print('Директория изменена на: ' + os.path.abspath(os.curdir))


if __name__ == '__main__':
    # create_file('test.txt', 'test text')
    # create_folder('test_folder2')
    get_list()
    # get_list(True)
    # delete_file_or_folder('белиберда')
    # delete_file_or_folder('test_folder2')
    # delete_file_or_folder('test.txt')
    # copy_file_or_folder('test_folder2', 'test_folder3_copy')
    # copy_file_or_folder('testdfg.txt', 'test(copy).txt')
    # save_info('asf')
    # change_current_dir('ds')
