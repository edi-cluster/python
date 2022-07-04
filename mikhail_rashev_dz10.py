#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:28:51 2022
mikhail_rashev_dz10.py
Михаил рашев. Домашнее задание 10.
@author: rashev
"""

from abc import ABC, abstractmethod
import math
from random import randrange

# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |

# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |

# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и пр.
print("\nДЗ 10.1\n")


class Matrix():
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for row in self.lst:
            cur_str = ""
            for val in row:
                cur_str += " " + str(val)
            print(cur_str)

        return ""

    def __add__(self, lst2):
        lst1 = self.lst
        lst2 = lst2.lst
        lst3 = lst1
        len_i = len(lst1)
        len_j = len(lst1[0])

        for i in range(len_i):
            for j in range(len_j):
                lst3[i][j] = lst1[i][j] + lst2[i][j]

        lst3 = Matrix(lst3)

        return lst3

    def print_matrix(self, mtrx):
        self.__str__(mtrx)


lst1_1 = [[31, 22], [37, 43], [51, 86]]
lst1_2 = [[21, 28], [17, 53], [44, 36]]
lst2_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
lst2_2 = [[8, 56, 65], [3, 8, 4], [32, 75, 7]]
lst3_1 = [[3, 5, 8, 3], [8, 3, 7, 1]]
lst3_2 = [[1, 8, 6, 9], [7, 4, 2, 4]]

print(f"матрицы для складывания:\n")
print(lst1_1)
print("   +   ")
print(lst1_2)
print("\n")
print(lst2_1)
print("   +   ")
print(lst2_2)
print("\n")
print(lst3_1)
print("   +   ")
print(lst3_2)

print(f"\n- Cоздаем 3 объекта класса Matrix - 3 матрицы\n")
mtrx1_1 = Matrix(lst1_1)
mtrx2_1 = Matrix(lst2_1)
mtrx3_1 = Matrix(lst3_1)

mtrx1_2 = Matrix(lst1_2)
mtrx2_2 = Matrix(lst2_2)
mtrx3_2 = Matrix(lst3_2)

print(f"- Cкладываем матрицы используя + и\
 распечатываем результат print() ...\n")
result1 = mtrx1_1 + mtrx1_2
print(f"Распечтываем результат 1 в обычном виде\
 при помощи функции print(matrix):")
print(result1)
print("\n")

result2 = mtrx2_1 + mtrx2_2
print(f"Распечтываем результат 2 в обычном виде\
 при помощи функции print(matrix):")
print(result2)
print("\n")

result3 = mtrx3_1 + mtrx3_2
print(f"Распечтываем результат 3 в обычном виде\
 при помощи функции print(matrix):")
print(result3)
# 2. Реализовать проект расчёта суммарного расхода ткани
# на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта
# и проверить работу декоратора @property.
print("\nД.З. 10.2\n")


class AbstractCoat(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_fabric_rate(self):
        pass


class AbstractSuit(ABC):
    @abstractmethod
    def __init(self):
        pass

    @abstractmethod
    def calc_fabric_rate(self):
        pass


class Odegda():
    def __init__(self):
        self.exemplars = {}
        self.amount = 0
        pass

    def add_odegda(self, obj):
        self.exemplars.update({obj.type: obj})
        self.amount = len(self.exemplars)

    @property
    def get_amount_exemplars(self):
        return self.amount

    def show_odegda(self):
        i = 0
        for item in self.exemplars:
            i += 1
            print(f"вещь №{i}: {item}")


class Coat(AbstractCoat):
    def __init__(self, title, size):
        self.type = "Пальто"
        self.title = title
        self.size = size

    def calc_fabric_rate(self):
        V = self.size
        formula = V/6.5 + 0.5

        return formula


class Suit:
    def __init__(self, title, height):
        self.type = "Костюм"
        self.title = title
        self.height = height

    def calc_fabric_rate(self):
        H = self.height
        formula = H * 2 + 0.3

        return formula


name1 = "Вельветовое пальто"
size1 = 50

name2 = "Школьный костюм"
height2 = 178/100  # в метрах

print("Создаем обекты классов Odegda, Coat, Suit.")
moya_odegda = Odegda()
coat1 = Coat(name1, size1)
suit2 = Suit(name2, height2)
print(f"Добавляем {name1}, {name2} в наш гардероб класса Odegda")
moya_odegda.add_odegda(coat1)
moya_odegda.add_odegda(suit2)
print("\nРаспечатываем содержание гардероба:")
moya_odegda.show_odegda()
print("\nУзнаем расход ткани в метрах ...")
result1 = coat1.calc_fabric_rate()
result2 = suit2.calc_fabric_rate()
print(f"для пальто : {result1:.2f}")
print(f"для костюма : {result2:.2f}")

print(f"\nПроверяем работу @property для функции obj.get_amount_exemplar ")
num_odegda = moya_odegda.get_amount_exemplars
print(f"атрибут moya_odegda.get_amount_exemplars = {num_odegda}")
# 3. Осуществить программу работы с органическими клетками,
# состоящими из ячеек.
# Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и округление до целого числа деления клеток,
# соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять,
# только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух.
# Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает,
#  то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
#  Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
print("\nД.З. 10.3\n")


class Medium:
    def __init__(self, subst):
        self.num_of_id = 0
        self.substr = subst
        self.cells = {}

    def add_cell(self, cell):
        self.num_of_id += 1
        cell.id = self.num_of_id
        self.cells.update({cell.id: cell})

        return cell.id

    def grow_cells(self, duration):
        """
        Выращиваем клетки в течении времени duration,
        так как процесс статисический, моделируем ситуацию с помощью библиотеки
        random
        """
        rand_val = randrange(duration)
        day_sec = 60*60*24
        growth_rate = int(1 + rand_val/day_sec)
        print(self.cells.keys())
        for key in self.cells.keys():
            self.cells[key].bins = self.cells[key].bins * growth_rate


class Cell:
    def __init__(self, cname, bins, rownum):
        self.id = 0
        self.cname = cname  # название клетки
        self.bins = bins  # количестао ячеек
        self.rownum = rownum  # число в ряду

    def __add__(self, obj):
        self.bins += obj.bins

        return self.bins

    def __sub__(self, obj):
        self.bins -= obj.bins
        if self.bins < 0:
            self.bins = 0
            print("После вычитания количество ячеек в клетке 1, < 0")

        return self.bins

    def __mul__(self, obj):
        self.bins = self.bins * obj.bins

        return self.bins

    def __floordiv__(self, obj):
        self.bins = math.floor(self.bins / obj.bins)

        return self.bins

    def __truediv__(self, obj):
        self.bins = self.bins / obj.bins

        return self.bins

    def make_order(self):
        sequence = ""
        rows = int(self.bins / self.rownum)
        remainder = self.bins % self.rownum

        for i in range(rows):
            for j in range(self.rownum):
                sequence += "*"
            sequence += "\n"

        for i in range(remainder):
            sequence += "*"
        print(repr(sequence))


nbins1 = 5
rownum1 = 7
nbins2 = 4
rownum2 = 8

days = 3
days2grow = days * 60*60*24  # int количество дней в секундах

mediumname = "amino acid auxotrophies"
cellname = "Escherichia coli"

print(f"Создаем спитательную среду {mediumname} для клеток")
md1 = Medium(mediumname)
print(f"Создаем две клетки {cellname}\n")
cl1 = Cell(cellname, nbins1, rownum1)
print(f"После создания клетка 1 имеет параметры: ячеек - {nbins1},\
 ячеек в ряду - {rownum1}")
cl2 = Cell(cellname, nbins2, rownum2)
print(f"После создания клетка 2 имеет параметры: ячеек - {nbins2},\
 ячеек в ряду - {rownum2}")
id1 = md1.add_cell(cl1)
id2 = md1.add_cell(cl2)
print(f"\nПусть клетки подрастут в течении {days}\
 дней при помощи функции grow_cells(секунд)")
md1.grow_cells(days2grow)
print(f"клетка 1 имеет параметры: ячеек - {cl1.bins},\
 ячеек в ряду - {rownum1}")
print(f"клетка 2 имеет параметры: ячеек - {cl2.bins},\
 ячеек в ряду - {rownum2}")

cl1 + cl2
print(f"\nСкладываем + , клетка 1 имеет параметры: ячеек - {cl1.bins}")
cl1 - cl2
print(f"\nВычитаем - , клетка 1 имеет параметры: ячеек - {cl1.bins}")
cl1 * cl2
print(f"\nУмножаем * , клетка 1 имеет параметры: ячеек - {cl1.bins},\
 ячеек в ряду - {rownum1}, остаток * - {cl1.bins%rownum1}")
print(f"\nВызываем Cell.make_order(), клетка 1 имеет следующую\
 последовательность:")
cl1.make_order()
cl1 // cl2
print(f"\nДелим //, клетка 1 имеет параметры: ячеек - {cl1.bins}")
cl1 / cl2
print(f"\nДелим /, клетка 1 имеет параметры: ячеек - {cl1.bins}")
