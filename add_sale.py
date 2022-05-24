#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:18:39 2022
add_sale.py
Создание файла bakery.csv
Добавление записей продаж в виде:
    номер_записи дата сумма
запуск скрипта:
    python add_sale 1234 дата_продажи
@author: rashev
"""

import sys
import os
from datetime import date


def read_args():
    num_arg = len(sys.argv[1:])
    value = sys.argv[1]
    cur_date = "yyyy-mm-dd"
    print(f"входные данные - число продаж, дата должны быть\
 в виде XXXX {cur_date}")

    if num_arg == 1:
        cur_date = date.today().strftime("%Y-%m-%d")
    elif num_arg == 2:
        cur_date = sys.argv[2]
    else:
        print(f"число входящих аргументов должно быть 1 или 2")

    return (value, cur_date)


def find_last_record_num(file_name):
    content = []
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.readlines()

    return len(content)


print("ДЗ 6.6 добавление записей в файл bakery.csv")
fname = "bakery.csv"
full_name = os.getcwd() + "/" + fname
val, tdate = read_args()
cur_rec_num = 1
print(f"путь к файлу {fname} - {full_name}")

if os.path.exists(full_name):
    cur_rec_num = find_last_record_num(full_name) + 1

with open(fname, 'a', encoding='utf-8') as f:
    record = str(cur_rec_num) + " " + tdate + " " + str(val) + "\n"
    f.write(record)
