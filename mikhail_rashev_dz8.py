#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:54:05 2022
mikhail_rashev_dz8.py
Михаил Рашев, Домашнее задание 8.
@author: rashev
"""

import re
from functools import wraps

# Урок 8. Декораторы
# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  ...
#    raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их
# в регулярном выражении; имеет ли смысл в данном случае использовать
# функцию re.compile()?
print("ДЗ 8.1")


def email_parse(eadres, pt, pt_valid_u, pt_valid_d):
    tdict = {'username': '',
             'domain': ''
             }
    try:
        str_parse = ptn.match(eadres)
        tdict['username'] = str_parse[1]
        tdict['domain'] = str_parse[2]
    except Exception as e:
        print(f"Ошибка №1 в функции при разборе емайла {eadres}, {e}")
    try:
        parse1 = pt_valid_u.match(tdict['username'])
        parse2 = pt_valid_d.match(tdict['domain'])

        if parse1 is None:
            raise ValueError(f"Ошибка в имени пользователя\
 {tdict['username']}")
            print(f"p1-{parse1}")
        elif parse2 is None:
            raise ValueError(f"Ошибка в имени пользователя {tdict['domain']}")
        else:
            pass
    except Exception as e:
        print(f"Ошибка №2 в функции при разборе емайла {eadres}, {e}")

    return tdict


email1 = "perelmann@mail.ru"
email2 = "perelmann~@mail.ru"
ptn = re.compile(r'(.+)@(.+)')
ptn_valid_u = re.compile(r'^[\w\-_\.]+$')
ptn_valid_d = re.compile(r'[A-Za-z0-9\.-_]+\.[A-Za-z]{2,}$')


print(f"Делаем разбор email - {email1} при помощи функции - email_parse")
print("на выходе получаем словарик result{username: xxx, domain: xxx}")
result = email_parse(email1, ptn, ptn_valid_u, ptn_valid_d)
print(result)

print(f"\nДелаем разбор email - {email2} при помощи функции - email_parse")
print("на выходе получаем словарик result{username: xxx, domain: xxx}")
result = email_parse(email2, ptn, ptn_valid_u, ptn_valid_d)
print(result)
# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/
# nginx_logs/nginx_logs) для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
# <response_code>, <response_size>), например:

# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000]
#  "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога
# в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

# 3. Написать декоратор для логирования типов позиционных аргументов функции,
# например:
# def type_logger...
#    ...

# @type_logger
# def calc_cube(x):
#   return x ** 3

# >>> a = calc_cube(5)

# 5: <class 'int'>
# Примечание: если аргументов несколько -
# выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
print("\nДЗ 8.3")


def type_logger(func):
    def wrapper(*args):
        print(f"количество аргументов: {len(args)}")
        print("Распечатываем каждый...")
        for each in args:
            print(f"{each}: {type(each)}")
        return [func(each) for each in args]
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


def type_logger2(func):
    @wraps(func)
    def wrapper(*args):
        print(f"количество аргументов: {len(args)}")
        print("Распечатываем вызов функции и тип аргумента...")
        for val in args:
            func_name = func.__name__
            print("{0}({1}: {2})".format(func_name, val, type(val)))
        return [func(each) for each in args]
    return wrapper


@type_logger2
def calc_cube2(x):
    return x ** 3


def type_logger3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"количество входных аргументов в словаре: {len(kwargs)}")
        print("Распечатываем вызов функции и тип аргумента...")
        print(f"все значения из словаря - {kwargs}")
        for key in kwargs.keys():
            val = kwargs.get(key)
            func_name = func.__name__
            print(f"ключ - {key}, значение - {val}")
            print("{0}({1}: {2})".format(func_name, val, type(val)))
        return [func(kwargs.get(each)) for each in kwargs.keys()]
    return wrapper


@type_logger3
def calc_cube3(a=1, b=1):
    return a ** 3 + b ** 3


print("Начинаем логирование работы функции calc_cube()")
res1 = calc_cube(2, 3, 4)
print(f"\nres1 = {res1}")

print("\nНачинаем логирование работы функции calc_cube2()")
res2 = calc_cube2(2, 3, 4)
print(f"\nres2 = {res2}")

print("\nНачинаем логирование работы функции calc_cube3()")
res3 = calc_cube3(a=2, b=3)
print(f"\nres3 = {res3} *")
print("*используется значение параметра b=1 по умолчанию [2^3+1, 3^3+1]")
# 4. Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение
# ValueError, если что-то не так, например:
# def val_checker...
#    ...


# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#   return x ** 3


# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#  ...
#    raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
print("\nДЗ 8.4")


def val_checker1(val):
    def _val_checker1(func):
        @wraps(func)
        def wrapper(args):
            a = val(args)
            try:
                if a is True:
                    return func(args)
                else:
                    msg1 = f"!!!, значение {args} не является целым числом."
                    msg2 = " пожалуста , поменяйте аргумент на"
                    msg3 = " положительное число"
                    raise ValueError(msg1 + msg2 + msg3)
            except Exception as e:
                print(e)
        return wrapper
    return _val_checker1


@val_checker1(lambda x: x > 0)
def calc_cubes(x1):
    return x1 ** 3


a = 2
print(f"\nЗапускаем функцию calc_cubes с аргументом: {a}")
res = calc_cubes(a)
print(f"результат - {res}")

b = -2
print(f"\nЗапускаем функцию calc_cubes с аргументом: {b}")
res = calc_cubes(b)
print(f"результат - {res}")
