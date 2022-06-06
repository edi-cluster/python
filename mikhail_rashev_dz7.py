#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:46:22 2022
Михаил Рашев, Домашнее Задание 7.
решены задачи 1, 3, 4
@author: rashev
"""

import os
from shutil import copy2

# 1. Написать скрипт, создающий стартер (заготовку)
# для проекта со следующей структурой папок:

# |--my_project
#  |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
print("\nДЗ 7.1\n")


def create_top(top, sep, fd_name):
    """
    create_top создает корневую папку проекта
    """
    full_name = top + sep + fd_name
    if not os.path.exists(full_name):
        os.mkdir(full_name)
    else:
        print(f"папка {fd_name} уже существует")
        print(f"путь к ней - {top}\n")
        # exit(1)


def read_config(fd_names, separ):
    """
    read_config() конвертирует сепаратор каталогов для данной ос, для входной
    структуры данных
    """
    tdict = fd_names
    for name in tdict.keys():
        tdict[name] = tdict[name].replace("/", separ) + separ
    return tdict


def create_tree(folders, pr_name):
    """
    create_tree создает структуру каталогов из словаря на входе
    """
    names = (name for name in folders.keys() if name != pr_name)
    for name in names:
        full_name = folders.get(name)
        if not os.path.exists(full_name):
            try:
                os.makedirs(full_name)
            except Exception as e:
                print(e)
                print("Ошибка в создании структуры папок")


def show_struct(path_in):
    res = []
    for rootdir, dirs, files in os.walk(path_in):
        for subdir in dirs:
            res.append(os.path.join(rootdir, subdir))

    return res


# структура папок
# config структура в виде словарика
folders = {
        "project_name": "my_project_uniq",
        "settings": "my_project_uniq/settings",
        "mainapp":  "my_project_uniq/settings/mainapp",
        "adminapp": "my_project_uniq/settings/adminapp",
        "authnapp": "my_project_uniq/settings/authapp"
        }

# устанавливаем переменные для работы с каталогами
root = os.getcwd()
cur_dir = root
sep = os.sep
os.chdir(cur_dir)
# читаем входные данные
folders_new_os = read_config(folders, sep)
project_name = folders.get("project_name")
# создаем структуру каталогов
create_top(cur_dir, sep, project_name)
create_tree(folders_new_os, project_name)
print(f"Структура папок {project_name}, сканируем ее")
for line in show_struct(root):
    print(line)
# добавить каталоги
# меняем структуру "config" словаря folders
new_admin_path = "my_project_uniq/settings/new_adminapp/"
old_admin_path = folders.get("adminapp")
folders.update({"old_adminapp": old_admin_path})
folders.update({"adminapp": new_admin_path})
# обновляем структуру каталогов
cur_dir = os.path.join(root, project_name) + "settings"
os.chdir(cur_dir)
os.rename("adminapp", "oldadminapp")
if not os.path.exists("new_adminapp"):
    os.mkdir("new_adminapp")

# Сохранить структуру каталогов в файл
struct = show_struct(root)
fname = project_name.replace("/", "") + ".readme"
with open(fname, 'w') as f:
    for line in struct:
        f.write(line + "/n")


# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
# (как быть?); как лучше хранить конфигурацию этого стартера,
# чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о
# вложенных папках и файлах (добавлять детали)?

# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер
# для проекта со следующей структурой:

# |--my_project
#   |--settings
#   |  |--__init__.py
#   |  |--dev.py
#   |  |--prod.py
#   |--mainapp
#   |  |--__init__.py
#   |  |--models.py
#   |  |--views.py
#   |  |--templates
#   |     |--mainapp
#   |        |--base.html
#   |        |--index.html
#   |--authapp
#   |  |--__init__.py
#   |  |--models.py
#   |  |--views.py
#   |  |--templates
#   |     |--authapp
#   |        |--base.html
#   |        |--index.html

# Примечание: структуру файла config.yaml придумайте сами,
# его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации,
# библиотеки использовать нельзя.

# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике).
# Написать скрипт,
# который собирает все шаблоны в одну папку templates, например:

# |--my_project
#   ...
#  |--templates
#   |   |--mainapp
#   |   |  |--base.html
#   |   |  |--index.html
#   |   |--authapp
#   |      |--base.html
#   |      |--index.html

# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные
# исключительные ситуации; это реальная задача, которая решена,
# например, во фреймворке django.

print("\nДЗ 7.3\n")
os.chdir(root)
print(os.listdir(root))


def create_folder_struct(sepa):
    '''
    create_folder_struct
    создает структуру каталогов
    '''
    lines = []
    l1 = "my_project2" + sepa
    l2 = l1 + "settings" + sepa
    l3 = l2 + "__init__.py"
    l4 = l2 + "dev.py"
    l5 = l2 + "prod.py"
    l6 = l1 + "mainapp" + sepa
    l7 = l6 + "__init__.py"
    l8 = l6 + "models.py"
    l9 = l6 + "views.py"
    l10 = l6 + "templates" + sepa
    l11 = l10 + "mainapp" + sepa
    l12 = l11 + "base.html"
    l13 = l11 + "index.html"
    l14 = l1 + "authapp" + sepa
    l15 = l14 + "__init__.py"
    l16 = l14 + "models.py"
    l17 = l14 + "views.py"
    l18 = l14 + "templates" + sepa
    l19 = l18 + "authapp" + sepa
    l20 = l19 + "base.html"
    l21 = l19 + "index.html"

    lines.append(l1)
    lines.append(l2)
    lines.append(l3)
    lines.append(l4)
    lines.append(l5)
    lines.append(l6)
    lines.append(l7)
    lines.append(l8)
    lines.append(l9)
    lines.append(l10)
    lines.append(l11)
    lines.append(l12)
    lines.append(l13)
    lines.append(l14)
    lines.append(l15)
    lines.append(l16)
    lines.append(l17)
    lines.append(l18)
    lines.append(l19)
    lines.append(l20)
    lines.append(l21)

    for cur_l in lines:
        if cur_l.endswith(("py", "html")) is True:
            dirs, filename = os.path.split(cur_l)
            if not os.path.exists(cur_l):
                try:
                    with open(cur_l, 'w') as f:
                        pass
                except Exception as e:
                    print(e)
                    print("Ошибка в создании структуры файлов")
        else:
            if not os.path.exists(cur_l):
                try:
                    os.makedirs(cur_l)
                except Exception as e:
                    e.find("")
                    print(e)
                    print("Ошибка в создании структуры папок")


def move_to_templates(full_name, copy_dir, cur_dir, sepa):
    exit_code = 0
    dirs, cur_file = os.path.split(full_name)
    copy_folder = dirs.split("/")[-1]
    create_dir = copy_dir + sepa + copy_folder
    create_dir_file = create_dir + sepa + cur_file
    if not os.path.exists(create_dir):
        os.makedirs(create_dir)
    try:
        copy2(full_name, create_dir_file)
    except Exception as e:
        cur_str = str(e).find("are the same file")
        if cur_str != 198 and cur_str != 196:
            print(f"\n Error in move_to templates - {e}\n")
            exit_code = 1
        else:
            pass

    return exit_code


create_folder_struct(sep)
cur_dir = root + sep + "my_project2"
os.chdir(root + sep + "my_project2")
create_dir = cur_dir + sep + "templates"
print(f"создаем директорию templates/ в my_project2")
if not os.path.exists(create_dir):
    os.makedirs(create_dir)

for dirpath, dirs, files in os.walk(cur_dir):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if fname.find(create_dir) is True:
            continue
        if fname.endswith('html'):
            print(f"копируем html файл - {fname} в templates/")
            result = move_to_templates(fname, create_dir, cur_dir, sep)
            if result == 1:
                print("Ошибка в корировании файла\n")

# 4. Написать скрипт, который выводит статистику
# для заданной папки в виде словаря, в котором ключи —
# верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей
# (начинаем с 0), например:

#    {
#      100: 15,
#      1000: 3,
#      10000: 7,
#      100000: 2
#    }

# Тут 15 файлов размером не более 100 байт;
# 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

print("\nДЗ 7.4\n")


def stat_folder(folder):
    tdict = {100: 0, 1000: 0, 10000: 0, 100000: 0}
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            if fname.endswith('.html'):
                size = os.stat(fname).st_size
                if size < 101:
                    tdict[100] = tdict[100] + 1
                elif size > 100 and size < 1001:
                    tdict[1000] = tdict[1000] + 1
                elif size > 1000 and size < 10001:
                    tdict[10000] = tdict[10000] + 1
                else:
                    pass

    return tdict


home = os.path.expanduser("~")
print(f"ожидается большое количество файлов, поэтому ищем например html")
print(f"ищем файлы в папке home - {home}")
os.chdir(home)

result = stat_folder(home)
print(f" Вывод на экран - словарик, размер в байтах : количество файлов,\
 меньше этого размера")
print(result)


# 5. * (вместо 4) Написать скрипт, который выводит статистику
# для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]),
# например:

#  {
#      100: (15, ['txt']),
#      1000: (3, ['py', 'txt']),
#      10000: (7, ['html', 'css']),
#      100000: (2, ['png', 'jpg'])
#    }

# Сохраните результаты в файл <folder_name>_summary.json в той же папке,
# где запустили скрипт.
