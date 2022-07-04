#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:57:25 2022
mikhail_rashev_dz9.py
Михаил Рашев, Домашнее задание 9.
@author: rashev
"""

import time
from datetime import datetime
from random import randrange

# 1. Создать класс TrafficLight (светофор):
# - определить у него один атрибут color (цвет) и метод running (запуск);
#  атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);

# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
print("ДЗ 9.1")


class TrafficLight():
    def __init__(self, colors, durations):
        self._color = "red"
        self._duration = 1
        self.colors = colors
        self.durations = durations
        self.start_time = time.perf_counter()
        self.current_run_time = 0

    def running(self, test=30):
        '''
        запускает работу свеотфора,
        устанавливает цвет и проверяет порядок следования цвета через функцию
        _test_colors_order(self, clrs)
        '''
        test_colors = []  # для проверки следования цветов
        i = 0

        if test:
            print(f"\nCветофор работает в тестовом режиме в \
течение - {test} секунд\n")

        while i < 10:
            self._color = self.colors[i]
            self._duration = self.durations[i]
            # запускаем светофор: устанавливаем цвет и его продолжительность
            self._set_color()
            time.sleep(self._duration)

            i += 1

            test_colors.append(self._color)
            if i > 2:
                answ = self._test_colors_order(test_colors)
                if not answ:
                    print(f"Нарушен порядок следования цветов -{time.now()}")
                    break
                else:
                    pass

                i = 0
                test_colors = []
            else:
                pass

            # записываем время работы светофора в self.current_run_time
            self.current_run_time = self.run_time()
            if test:
                if self.current_run_time > test:
                    print(f"\nАктуальное время тестирования светофора -\
 {self.current_run_time:.1f} секунд, закончилось.")
                    break
        return 0

    def _set_color(self):
        clr = self._color

        if clr == "Красный":
            msg = "\033[31m {0}".format(clr)
        elif clr == "Желтый":
            msg = "\033[30m {0}".format(clr)
        elif clr == "Зеленый":
            msg = "\033[32m {0}".format(clr)
        else:
            msg = "Error"
        print(msg)

        msg = " \033[0m"  # сброс цвета

    def run_time(self):
        t21 = time.perf_counter() - self.start_time

        return t21

    def _test_colors_order(self, clrs):
        for i in (0, 1, 2):
            if self.colors[i] != clrs[i]:
                return 0
        return 1


test_run = 15  # 10 seconds

# Чтобы не ошибиться заводим пары цвет: время в словарик clrs_durs
clrs_durs = {
       "Красный": 7,
       "Желтый": 2,
       "Зеленый": 5
       }
cur_clrs = ("Красный", "Желтый", "Зеленый")
cur_durs = [clrs_durs[clrs] for clrs in cur_clrs]
print(f"\nЧтобы не ошибиться заводим пары (цвет: время в секундах)\
 в словарик:\n{clrs_durs}")
print(f"В cur_clrs определяется порядок следования цветов {cur_clrs}")
print("Переменная test_run, если задана, определяет время работы светофора.")
print("Запускаем светофор...")
svetofor = TrafficLight(cur_clrs, cur_durs)
svetofor.running(test_run)


# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого
# для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта
# для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;

# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
print("\nДЗ 9.2\n")


class Road():
    def __init__(self, gst, price, rho, length=1, width=0, thickness=0):
        self._length = length
        self._width = width
        self._thickness = thickness
        self._price = price
        self._gost = gst
        self._rho = rho

    def price_calc(self, cur_length):
        volume = self._width * self._thickness * self._length
        total_price = volume * self._price

        return total_price

    def price_calc_gost(self, cur_length):
        volume = self._gost.get("width") * self._gost.get("lanes") *    \
            self._gost.get("thickness") * cur_length
        total_price = volume * self._price

        return total_price

    def asphalt_mass_calc(self, cur_length):
        volume = self._gost.get("width") * self._gost.get("lanes")  \
            * self._gost.get("thickness") * cur_length
        mass = volume * self._rho

        return mass


price_asp = 6200  # цена за м3
leng = 729 * 1000  # метров, Москва - Казань
thickn = 0  # метров
widths = 0  # метров

gost_highway = {
        "width": 3.75,  # meters
        "lanes": 4,
        "thickness": 0.12  # meters
        }

rho_aver = 1200  # кг/м3

print("Ширина дорог и толщина асфальта в России подчиняется регламенту\
 и расписаны в документе ГОСТ Р 52399-2005")
print(f"Примерные значения описаны в словаре gost_highway:\
 ширина полосы, количество полос, толщина асфальта:\n {gost_highway}")
print(f"Цена асфальта - {price_asp} рублей за 1 метр3, Мелкозернистый,\
 плотный, тип Б, М-1")
print(f"средняя плотность - {rho_aver} кг/м3")
print("(Данные из google запроса: асфальт цена м3 .)")
print("\nНачинаем расчет массы асфальта и стоимости...")
leng_default = 1  # метр
print("Создаем объект Road")
rd = Road(gost_highway, price_asp, rho_aver, leng_default, widths, thickn)
print("Вычисляем стоимость дороги в рублях...")
m12_price = rd.price_calc_gost(leng)
print("Вычисляем массу асфальта в килограммах...")
m12_asph_mass = rd.asphalt_mass_calc(leng)

print(f"Результат:\nцена асфальта для скоростной дороги\
 длиною {leng/1000} км - {m12_price:.1f} рублей, масса асфальта -\
 {m12_asph_mass:.1f} кг")


# 3. Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
#

# проверить работу примера на реальных данных:
# создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
print("\nДЗ 9.3\n")


class Worker():
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}

    def update_income(self, up_income):
        self._income.update(up_income)


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        text = f"{self.name} {self.surname},\
 {self.get_total_income()}: рублей"
        return text

    def get_total_income(self):
        return self._income

    def add_income(self, wage, bonus):
        up_income = {"wage": wage, "bonus": bonus}
        self.update_income(up_income)


class Organisation():
    def __init__(self, name, positions_ptn, bonus_ptn):
        self.posit_workers = []
        self.salary_table = positions_ptn
        self.cur_bonus = bonus_ptn.get("good_sales")

    def calculate_income(self, dep, posit):
        level1 = self.salary_table.get(dep)
        level2 = level1.get(posit)

        return level2

    def add_employee(self, obj_posit):
        position = obj_posit.position
        level1 = self.salary_table.get(position[0])
        wage = level1.get(position[1])
        obj_posit.add_income(wage, self.cur_bonus)
        self.posit_workers.append(obj_posit)

    def display_positions(self):
        for i in range(len(self.__posit_workers)):
            obj = self.__posit_workers[i]
            name = obj.name + " " + obj.surname
            print(f"имя - {name}, номер в организации -{i}")

    def monthly_salary(self, cur_id):
        person = self.posit_workers[cur_id]
        income = person.get_total_income()
        ret = (person.name, person.surname, income)

        return ret

    def pay_all(self):
        ret = []
        for i in range(len(self.posit_workers)):
            ret.append(self.monthly_salary(i))
        return ret


income_pattn = {
        "wage": 0,
        "bonus": 0,
        "date": datetime.now()
        }

position_ptn = {
        "инженер":
        {"разработка": 50000},
        "тим_лид":
        {"разработка": 60000},
        "кассир":
        {"продажи": 55000},
        "бухгалтер":
        {"администрация": 80000},
        "секретарь":
        {"администрация": 40000},
        "директор":
        {"администрация": 100000}
        }

bonus_ptn = {
        "end_year": 5000,
        "end_project": 2000,
        "good_sales": 1000
        }

name1 = "Александр"
surname1 = "Васильев"
position1 = ("инженер", "разработка")

name2 = "Алексей"
surname2 = "Быстров"
position2 = ("инженер", "разработка")

name3 = "Сергей"
surname3 = "Пенкин"
position3 = ("директор", "администрация")

name4 = "Елена"
surname4 = "Васильева"
position4 = ("инженер", "разработка")

name5 = "Ольга"
surname5 = "Котельникова"
position5 = ("секретарь", "администрация")

name6 = "Василий"
surname6 = "Петров"
position6 = ("бухгалтер", "администрация")

name7 = "Ирина"
surname7 = "Панова"
position7 = ("кассир", "продажи")

org_name = "МаленькаяКомпания"
print(f"Создаем организацию {org_name} (где работают сотрудники) -\
 объект класса Organisation\n")
org = Organisation(org_name, position_ptn, bonus_ptn)

print("Создаем 7 работников/объектов класса Position")
pst1 = Position(name1, surname1, position1)
print("Добавляем каждого работника в организацию.")
org.add_employee(pst1)
full_name = pst1.get_full_name()
print("Вызов функции Position.get_full_name():")
print(full_name + "\n")

pst2 = Position(name2, surname2, position2)
org.add_employee(pst2)

pst3 = Position(name3, surname3, position3)
org.add_employee(pst3)

pst4 = Position(name4, surname4, position4)
org.add_employee(pst4)

pst5 = Position(name5, surname5, position5)
org.add_employee(pst5)

pst6 = Position(name6, surname6, position6)
org.add_employee(pst6)

pst7 = Position(name7, surname7, position7)
org.add_employee(pst7)

pay_list = org.pay_all()
print(f"распечатать содержание 7 объектов типа Position, через функцию\
 Organisation.pay_all()\n")
print(f"расчетный список для организации {org_name}:\n")
for record in pay_list:
    text = "{0}, {1}, зарплата - {2} рублей, бонус - {3}\
    рублей".format(record[0], record[1], record[2].get("wage"),
                   record[2].get("bonus"))

    print(text)
# 4. Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# 3поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;

# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.
print("\nДЗ 9.4\n")


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.text = f"машина {self.name } цвета {self.color}"
        self.cur_speed = 0
        self.speed_range = 200

    def go(self):
        self.accelerate()
        print(self.text + " едет со скоростью " + str(self.cur_speed))

    def stop(self):
        self.cur_speed = 0
        print(self.text + " остановилась")

    def turn(self, direction):
        self.cur_speed = randrange(50)
        print(self.text + " повернула " + direction
              + " со скоростью " + str(self.cur_speed))

    def show_speed(self):
        msg = f"скорость - {self.cur_speed}"
        print(msg)

        return self.cur_speed

    def accelerate(self):
        self.cur_speed = randrange(self.speed_range)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed_limit = 60
        self.speed_range = 150

    def show_speed(self):
        speed = self.cur_speed

        if speed > self.speed_limit:
            msg1 = f"Вы превышаете допустимую скорость - {self.speed_limit}"
            msg2 = f"Ваша текущая скорость - {speed}"
            print(msg1)
            print(msg2)
        else:
            msg = f"скорость - {self.cur_speed}"
            print(msg)

        return self.cur_speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed_range = 300


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed_limit = 40
        self.speed_range = 90

    def show_speed(self):
        speed = self.cur_speed

        if speed > self.speed_limit:
            msg1 = f"Вы превышаете допустимую скорость - {self.speed_limit}"
            msg2 = f"Ваша текущая скорость - {speed}"
            print(msg1)
            print(msg2)
        else:
            msg = f"скорость - {self.cur_speed}"
            print(msg)

        return self.cur_speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed_range = 200


speed1 = 0
color1 = "белый"
name1 = "фиат"
is_police1 = False

speed2 = 0
color2 = "синий"
name2 = "лада"
is_police2 = False

speed3 = 0
color3 = "черный"
name3 = "shkoda"
is_police3 = False

speed4 = 0
color4 = "серый"
name4 = "mercedes s20"
is_police4 = False

speed5 = 0
color5 = "зеленый"
name5 = "wolkswagen passat"
is_police5 = True

print("Создаем 5 объектов на основе родительского класса Car\n")
cars = []
town_car = TownCar(speed1, color1, name1, is_police1)
cars.append(town_car)
work_car = WorkCar(speed2, color2, name2, is_police2)
cars.append(work_car)
work_car2 = WorkCar(speed3, color3, name3, is_police3)
cars.append(work_car2)
sport_car = SportCar(speed4, color4, name4, is_police4)
cars.append(sport_car)
police_car = PoliceCar(speed5, color5, name5, is_police5)
cars.append(police_car)

print("Едем на машине и затем распечатываем атрибуты...\n")
for cur_car in cars:
    cur_car.go()
    # cur_car.show_speed()
    cur_car.stop()
    cur_car.go()
    # cur_car.show_speed()
    directs = {1: "направо", 2: "налево"}
    for i in directs.keys():
        cur_car.turn(directs.get(i))
    # cur_car.show_speed()
    cur_car.stop()
    print(f"распечатываем все атрибуты класса {cur_car.__class__}")
    print(cur_car.__dict__)
    print("\n")
# 5. Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка).
#  Метод выводит
# сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;

# создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

print("\nДЗ 9.5\n")


class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        msg = "Запуск отрисовки: "
        print(msg)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        msg = "Запуск отрисовки: ручка"
        print(msg)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        msg = "Запуск отрисовки: карандаш"
        print(msg)


class Handel(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        msg = "Запуск отрисовки: маркер"
        print(msg)


title1 = "Pen"
title2 = "Pencil"
title3 = "Handle"

print("создаем три объекта на основе базового класса Stationery:\
 Pen, Pencil, Handle\n")
pn = Pen(title1)
pl = Pencil(title2)
hn = Handel(title3)

print("Для каждго класса вызываем метод draw()")
msg = "объект класса "
pn.draw()
print(msg + pn.title)
pl.draw()
print(msg + pl.title)
hn.draw()
print(msg + hn.title)
