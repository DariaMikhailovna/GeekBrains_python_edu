from core import save_info, copy_file_or_folder, delete_file_or_folder, get_list, create_folder, create_file, change_current_dir
import sys
import HW_3

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Укажите команду!!!')
    exit(1)


if command == 'list':
    get_list()
elif command == 'go_game':
    save_info('Начало игры')
    HW_3.start_game()
    save_info('Конец игры')
elif command == 'change_dir':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название новой директории')
    else:
        change_current_dir(name)
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название')
    else:
        delete_file_or_folder(name)
elif command == 'copy':
    try:
        name1 = sys.argv[2]
        name2 = sys.argv[3]
    except IndexError:
        print('Отсутствует название')
    else:
        copy_file_or_folder(name1, name2)
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('change_dir - изменить текущую директорию')
    print('go_game - начать игру "Угадай число"')

save_info('Конец')
