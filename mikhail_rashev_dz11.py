#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:02:33 2022
mikhail_rashev_dz11.py
Михаил Рашев Д.З. 11
Большое спасибо за проверку задание и советы!
@author: rashev
"""

from datetime import datetime
from time import perf_counter
import re
import time
# import os

# 1. Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod,
#  должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
print("\nД.З. 11.1\n")


class LocalDate:
    def __init__(self, datestr):
        self.datestr = datestr

    @classmethod
    def get_ddmmyyyy(cls, date_in):
        if not date_in.find("-"):
            print(f"Дата {date_in} должна быть в формате дд-мм-гггг")
            return 0

        ddmmyyyy = date_in.split("-")
        dd = int(ddmmyyyy[0])
        mm = int(ddmmyyyy[1])
        yyyy = int(ddmmyyyy[2])

        return (dd, mm, yyyy)

    @staticmethod
    def validate_date(day_int, month_int, year_int):
        """
        Все параметры могут быть только типа int
        day - 1-31
        month - 1-12
        year -  0 < year < 2023
        """
        ret = 1
        if type(day_int) is not int:
            print(f"{day_int}")
            ret = 0
        elif type(month_int) is not int:
            print(f"{month_int}")
            ret = 0
        elif type(year_int) is not int:
            print(f"{year_int}")
            ret = 0
        else:
            pass

        if month_int not in range(1, 12):
            print(f"Ошибка в введнном месяце - {month_int}")
            print("Пожалуйста введите дату заново.")
            return 0
        if year_int not in range(1, datetime.now().year+1):
            print(f"Ошибка в введнном годе - {year_int}")
            print("Пожалуйста введите дату заново.")
            return 0

        day_year_reg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_year_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        not_leap_year = year_int % 4

        if not_leap_year:
            days = day_year_reg[month_int-1]
        else:
            days = day_year_leap[month_int-1]

        if day_int not in range(1, days+1):
            print(f"Ошибка в введнном дне - {day_int}")
            print("Пожалуйста введите дату заново.")
            return 0

        return ret


date1 = "08-08-2022"
date2 = "01-05-2020"
date3 = "29-02-2019"
date4 = "28-02-2019"

result1 = LocalDate.get_ddmmyyyy(date1)
print(result1)
if LocalDate.validate_date(result1[0], result1[1], result1[2]):
    dt1 = LocalDate(date1)
    print("Объект dt1 класса LocaleDate создан")

result2 = LocalDate.get_ddmmyyyy(date2)
print(result2)
if LocalDate.validate_date(result2[0], result2[1], result2[2]):
    dt2 = LocalDate(date2)
    print("Объект dt2 класса LocaleDate создан")

result3 = LocalDate.get_ddmmyyyy(date3)
print(result3)
if LocalDate.validate_date(result3[0], result3[1], result3[2]):
    dt3 = LocalDate(date3)
    print("Объект dt3 класса LocaleDate создан")

result4 = LocalDate.get_ddmmyyyy(date4)
print(result4)
if LocalDate.validate_date(result4[0], result4[1], result4[2]):
    dt4 = LocalDate(date4)
    print("Объект dt4 класса LocaleDate создан")
    
time.sleep(1)
# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.
print("\nД.З. 11.2\n")


class LocalException(Exception):
    def __init__(self, text):
        self.text = text


vals1 = (-8, 4, 5, 6, 7, 8, 9, 8, 3, 5)
vals2 = (-1, 0, 1, 3, 2, 0, 4, 2, 0, 1)

print(f"Поэлементно делим массив1 на массив2")
print(vals1)
print(vals2)
print("\n")

result = 1  # сохраняем результат последнего деления

for i in range(len(vals1)):
    try:
        if vals2[i] == 0:
            raise LocalException(f"Ошибка, деление на ноль,\
 {vals1[i]} / {vals2[i]} ")
        result = vals1[i]/vals2[i]
    except LocalException as e:
        print(e)

print("\nВсе поделили, теперь делить на ноль можно, но только осторожно...")
print(f"результат последнего деления: {result}")

time.sleep(1)
# 3. Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
#  Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список
# необходимо только числами.
#  Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
#  пока пользователь сам не остановит работу скрипта, введя,
#  например, команду «stop». При этом скрипт завершается,
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить
#  только числа и строки. Во время ввода пользователем очередного элемента
#  необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести
# текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
print("\nД.З. 11.3\n")


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class LocalException2(Exception):
    def __init__(self, text):
        self.text = text


def get_remaining(trun, tdiff):
    if trun > tdiff:
        print(f"{style.UNDERLINE}Осталось {trun - tdiff} секунд.{style.RESET}")
    elif tdiff > tdiff:
        print("Время истекло.")


enters = []
flag_a = 1

t1 = perf_counter()
test_run = 20  # время работы программы

print("Наберем массив данных.")
print(f"{style.RED}Программа будет работать в течении {test_run}\
 секунд{style.RESET}")
while flag_a > 0:
    inp_data = input("Введите положительное число или команду stop :")

    if inp_data == "stop":
        break

    try:
        if not inp_data.isnumeric():
            raise LocalException(f"Ошибка, входные данные - \
 строка inp: {inp_data}")
        else:
            enters.append(inp_data)
    except LocalException as e:
        print(e)

    t2 = perf_counter()
    t21 = int(t2 - t1)
    get_remaining(test_run, t21)
    if t21 > test_run:
        break

print("\nВывод введенных данных:")
for i in range(len(enters)):
    if i < len(enters) - 1:
        print(enters[i], end=", ")
    elif i == len(enters) - 1:
        print(enters[i], end="")
    else:
        pass

print("\n")
time.sleep(1)
# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
#  Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
print("\nД.З. 11.4\n")


class OrgTechStore:
    def __init__(self, name):
        """
        Склад оргтехники,
        построен по типу:
           {
           org_name:
               model:
                   [num_items, obj]
           }

        """
        self.stores = {}

    def add_orgtech(self, orgtech):
        """
        Добавляет оргтехнику в каталог self.store
        если модель существует, увеличивает её количество на 1:
        {model: num+1, orgtech_obj}
        """
        ret = 0
        if not self.validate_orgtech_names(orgtech):
            print("Сообщение со склада: у техники отсутствует название\
 или модель. Не можем принять на склад!")
            return 0
        cat = orgtech.name
        model = orgtech.model
        ref1 = self.stores[cat]
        if not ref1.get(model):
            update = {model: [1, orgtech]}
            self.stores[cat].update(update)
        else:
            ref1[model][0] += 1

        return ret

    def add_catalogs(self, cat):
        update = {}
        self.stores.update({cat: update})

    def print_all_catalog(self):
        print("\nРаспечатываем каталог:")
        for k1, v1 in self.stores.items():
            print(k1)
            for k2, v2 in v1.items():
                print(f"    {k2} штук: {v2[0]}")

    def validate_orgtech_names(self, org):
        if org.name == "" or org.model == "":
            return 0
        else:
            return 1

    def test_org(self, org, plug_connect):
        ret = 0
        if org.do_function(plug_connect):
            print(f"Технический отдел: тестирование {org.name} {org.model}\
 проведено, техника работает.\n")
            ret = 1
        else:
            print(f"Технический отдел: тестирование {org.name}\
 {org.model} проведено, техника НЕ работает!\n")

        return ret

    @staticmethod
    def test_org_external(org, plug_connect):
        ret = 0
        if org.do_function(plug_connect):
            print(f"Технический отдел: тестирование {org.name} {org.model}\
 проведено, техника работает.\n")
            ret = 1
        else:
            print(f"Технический отдел: тестирование {org.name} {org.model}\
 проведено, техника НЕ работает!\n")

        return ret


class OrgTech:
    def __init__(self, model):
        self.name = ""
        self.model = ""

    def do_function():
        pass


class Printer(OrgTech):
    def __init__(self, model, cur_type):
        self.name = "Принтер"
        self.model = model
        self.type = cur_type

    def do_function(self, plugin):
        ret = 0
        if plugin == "подключен к ПК":
            ret = 1
            text = f"{self.name} - {self.model} печатает ..."
        else:
            text = f"Звук {self.model} - Ох-ох"

        print(text)

        return ret


class Scanner(OrgTech):
    def __init__(self, model, file_format, optical_resolution):
        self.name = "Сканнер"
        self.model = model
        self.file_format = file_format
        self.optical_resolution = optical_resolution

    def do_function(self, plugin):
        ret = 0
        if plugin == "подключен к ПК":
            ret = 1
            text = f"{self.name} - {self.model} сканирует ..."
        else:
            text = f"Звук {self.model} - Ай-ай"

        print(text)

        return ret


class Xerox(OrgTech):
    def __init__(self, model, cur_type, optical_resolution):
        self.name = "Ксерокс"
        self.model = model
        self.type = cur_type
        self.optical_resolution = optical_resolution

    def do_function(self, plugin):
        ret = 0
        if plugin == "подключен к ПК":
            ret = 1
            text = f"{self.name} - {self.model} делает копию ..."
        else:
            text = f"Звук {self.model} - Ой-ой"
        print(text)

        return ret


# Данные
printermodel1 = "Canon A328E"
typeprinter1 = "laser"

printermodel2 = ""

scannermodel1 = "Epson WorkForce ES-50"
fformatscanner1 = "JPG, PNG, PDF"
optresolscanner1 = "800x1200"

xeroxmodel1 = "HP LaserJet 700"
typexerox1 = "laser"
optresolxerox1 = "1200x1800"

catalogs = ["Принтер", "Сканнер", "Ксерокс"]
store_name = "Эльбрус"

connect = "подключен к ПК"
not_connect = "не подключен к ПК"

# Объекты
print("Создаём объекты, наполняем их данными ...")
store = OrgTechStore(store_name)
for cat in catalogs:
    store.add_catalogs(cat)

print("Создаём Принтер, Сканнер, Ксерокс")
printer1 = Printer(printermodel1, typeprinter1)
scanner1 = Scanner(scannermodel1, fformatscanner1, optresolscanner1)
xerox1 = Xerox(xeroxmodel1, typexerox1, optresolxerox1)

print("Добавляем их на склад OrgTechStore")
store.add_orgtech(printer1)
store.add_orgtech(printer1)
store.add_orgtech(scanner1)
store.add_orgtech(scanner1)
store.add_orgtech(scanner1)
store.add_orgtech(xerox1)

print("\nСоздаём Принтер без названия модели")
printer2 = Printer(printermodel2, typeprinter1)
print("Пытаемся добавить на склад ...")
store.add_orgtech(printer2)

# Другое :)
store.print_all_catalog()
print(f"\nТестируем технику c объекта склад класса OrgTechStore ...\n")
store.test_org(printer2, connect)
store.test_org(printer1, not_connect)
store.test_org(scanner1, connect)
store.test_org(xerox1, connect)

print(f"\nТестируем технику c помощью\
 @staticmethod test_org_external(printer1, connect) ...\n")
OrgTechStore.test_org_external(printer1, connect)

time.sleep(1)
# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
print("\nД.З. 11.5\n")

print("Сделано в предыдущем задании 11.4. ")
print("OrgTechStore: словарь для хранения оргтехники - self.stores = {},\
 функции добавления - add_orgtech(orgtech), add_catalogs(cat) и\
 просмотра - print_all_catalog()")
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
print("\nД.З. 11.6\n")

print("Сделано в предыдущем задании 11.4. ")
print("Добавлена функция - validate_orgtech_names(org),\
 test_org(org, plug_connect), @staticmethod test_org_external")
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
print("\nД.З. 11.6\n")


class ComplexNumber:
    def __init__(self, val):
        self.ptn = re.compile(r'(\d{1,})([-,+]\d{1,})i')
        self.val = self.make_tuple_from_val(val)

    def __add__(self, val_in):
        val = val_in.val
        real = int(self.val[0]) + int(val[0])
        img = int(self.val[1]) + int(val[1])

        ret = str(real) + str(img) + "i"

        return (ret)

    def __sub__(self, val_in):
        val = val_in.val
        real = int(self.val[0]) - int(val[0])

        img = int(self.val[1]) - int(val[1])

        if img > 0 or img == 0:
            ret = str(real) + "+" + str(img) + "i"
        else:
            ret = str(real) + str(img) + "i"

        return (ret)

    def validate_entry(self, val_in):
        val = val_in
        ret = 0
        try:
            result = self.ptn.findall(val)[0]
            if not result:
                print("Пожалуйста проверьте корректность записи\
 комплексного числа {val}, ожидается запись вида 1+2i, -1-3i и подобные")
                ret = 0
            else:
                ret = 1
        except Exception as e:
            print(e)

        return ret

    def make_tuple_from_val(self, val):
        ptn = re.compile(r'([+-]{0,1}\d{1,})([-,+]\d{1,})i')
        result = ptn.findall(val)

        return result[0]

    @staticmethod
    def validate_entry_external(val):
        ret = 0
        try:
            ptn = re.compile(r'^([+-]{0,1}\d{1,})([-,+]\d{1,})i$')
            result = ptn.findall(val)

            if not result:
                print(f"Пожалуйста проверьте корректность записи\
 комплексного числа {val}, ожидается запись вида 1+2i, -1-3i и подобные им!\n")
                ret = 0
            else:
                ret = 1
        except Exception as e:
            print(e)

        return ret


num1 = "-111+2i"
num2 = "2-4i"
num3 = "-4-3i"
num4 = "-144-357i"

print(f"Комплексные числа num1, num2, num3, num4 в формате строка\
 на линиях 558-561:\n    {num1}, {num2}, {num3}, {num4}\n")

print("Поочередно проверяем формат комплексного чисел и создаем объекты\
 комплексных чисел.")
print("Допустимый формат записи - имеет вид -1+12i, 1000-10001i")
if ComplexNumber.validate_entry_external(num1):
    val1 = ComplexNumber(num1)
else:
    print(f"объект {num1} типа ComplexNumber was not created")

if ComplexNumber.validate_entry_external(num2):
    val2 = ComplexNumber(num2)
else:
    print(f"объект {num2} типа ComplexNumber was not created")

if ComplexNumber.validate_entry_external(num3):
    val3 = ComplexNumber(num2)
else:
    print(f"объект {num3} типа ComplexNumber was not created")

if ComplexNumber.validate_entry_external(num4):
    val4 = ComplexNumber(num4)
else:
    print(f"объект {num4} типа ComplexNumber was not created")

print("\nПроводим операции сложения + и вычитания - :")
v5 = val1 + val2
print(f" ({num1}) + ({num2}) = {v5}")

v6 = val3 - val4
print(f" ({num3}) - ({num4}) = {v6}")
