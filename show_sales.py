#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:16:22 2022
show_sales.py
показывает сумму продаж
запуск:
    python show_sales.py - все записи
    python show_sales.py num1
    python_show_sales.py num1 num2
num1, num2 - номер записи
@author: rashev
"""

import sys


def read_content(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()

    return content


arg = sys.argv[1:]
num_arg = len(arg)

fname = "bakery.csv"
records = read_content(fname)
text = ""

begin_rec = 0
end_rec = len(records) - 1

if num_arg == 0:
    text = f"Показывам все продажи"
elif num_arg == 1:
    begin_rec = int(arg[0]) - 1
    text = f"Показывам все продажи, начиная с записи номер = {begin_rec + 1}"
elif num_arg == 2:
    begin_rec = int(arg[0]) - 1
    end_rec = int(arg[1])
    text = f"Показывам все продажи, начиная с записи номер : {begin_rec + 1}\
 и заканчивая записью номер = {end_rec}"
else:
    print(f"Ошибка, число входящих аргументов должно быть 0, 1 или 2")
    print("Завершение программы...")
    exit(1)

print(f"Исходный файл - {fname}")
print(text)
for rec in records[begin_rec:end_rec]:
    rec_ar = rec.split(" ")
    rec = rec_ar[2].replace("\n", "") + "," + rec[0]
    print(f"{rec}")
