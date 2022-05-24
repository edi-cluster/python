#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:32:55 2022
Михаил Рашев.
Домашнее Задание 5. Генераторы и comprehensions. Множества.
@author: rashev
"""


# 1 Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1

print("\nЗадание 1 - генератор нечетных чисел с использованием yeild")


def odd_nums(num):
    num = num + 2
    for i in range(1, num, 2):
        yield i


# одна проверка
print("сначала генерируем объект odd_to_15(скорее это ссылка) и\
 выводим одно значение из объекта")
odd_to_15 = odd_nums(15)
print(next(odd_to_15))

print("снова генерируем объект и проводим все итерации")
num = 15
large_number = 1000
odd_to_15 = odd_nums(num)
for i in range(1, large_number):
    res = next(odd_to_15, "StopIteration")
    print(f"итерация - {i}, результат - {res}")
    if res == "StopIteration":
        break

# 2
print("\nЗадание 2 - генератор нечетных чисел без использования yeild")
num = 15
odd_to_15_2 = (i for i in range(1, num+2, 2))

# одна проверка
print("сначала генерируем объект odd_to_15_2 и\
 выводим одно значение из объекта")
print(next(odd_to_15_2))

print("снова генерируем объект и проводим все итерации")
num = 15
large_number = 1000
odd_to_15_2 = odd_nums(num)
for i in range(1, large_number):
    res = next(odd_to_15_2, "StopIteration")
    print(f"итерация - {i}, результат - {res}")
    if res == "StopIteration":
        break

# 3 Есть два списка,
# Необходимо реализовать генератор,
# возвращающий кортежи вида (<tutor>, <klass>), например:
print("\n Задание 3. реализовать генератор, возвращающий кортеж")


def generate_cortage(tut, klas):
    b = len(tut)
    for i in range(len(klas)):
        if i < b:
            yield (tut[i], klas[i])
        else:
            yield ("None", klas[i])


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
# Выводим значения
cortages = generate_cortage(tutors, klasses)
for i in range(len(klasses)+100):
    result = next(cortages, "StopIteration")
    print(f"итерация - {i+1}, значение - {result}")
    if result == "StopIteration":
        break

# 4. Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего
print("\n Задание 4. Представлен список чисел. Необходимо вывести \
те его элементы, значения которых больше предыдущего")
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(f"исходный список - {src}")
print(f"результат - {result}")

# 5. Представлен список чисел. Определить элементы списка,
# не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке
print("\n Задание 5. Представлен список чисел. Определить элементы списка, \
не имеющие повторений. Сформировать из этих элементов список \
с сохранением порядка их следования в исходном списке")
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def single_val(lst):
    '''
    вычисление чисел не имеющих повторений из последовательности.
    '''
    ret_lst = []
    for val in lst:
        if lst.count(val) == 1:
            ret_lst.append(val)

    return ret_lst


result = single_val(src)
print(f"исходный список - {src}")
print(f"результат1 - {result}\nфункция возвратила список\n")

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = (val for val in src if src.count(val) == 1)
print(f"исходный список - {src}")
print(f"результат2 - {result}, лучше по скорости и по памяти, но одноразовый")
# print all values
print("Выводим значения:")
result3 = (val for val in src if src.count(val) == 1)
[print(f"iter {i+1}", next(result3, "StopIteration"))
 for i in range(len(src)-4)]
