#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:32:27 2022
Михаил Рашев 
Домашнее задание 1
@author: rashev
"""

#import datetime as dt

def main():
    # 1. Домашнее задание №1. 
    # Реализовать вывод информации о промежутке времени 
    # в зависимости от его продолжительности duration в секундах
    duration(86521)
    # 2. Домашнее задание №2
    # Создать список, состоящий из кубов нечётных чисел от 1 до 1000    
    num_numbers = to_cube(0)
    print("число = кубов делящихся на 7 = ", num_numbers)
    num_numbers = to_cube(17)
    print("число = кубов делящихся на 7 = ", num_numbers)
    # 3. Домашнее задание №3
    declination_procents(21)
    

def duration(val):
    val_sec = 1
    val_min  = val_sec * 60 
    val_hour = val_min * 60
    val_day  = val_hour * 24
    val_year = val_day * 365
    #dur_year_leap = dur_day *366
    msg_sec = str(val*val_sec) + " секунды"
    msg_min = str( val//val_min ) + " минут и " + str(val%60) + " секунд"
    msg_hour = str(val//(60*60)) + " часов " + str(val%60) + " минут и " + str(val%60) + " секунд"
    msg_day = str(val//val_day) + " дней " + str( (val%(val_day))//val_hour ) + " часов " + str( ((val%(val_day))%val_hour)//val_min ) + " минут и " + str(val%60) + " секунд"
    msg_year = "какое то непонятпо большое время, явно больше года, нужно переходить на библиотеку datetime"
    msg_else = "не получается определить время, проверьте входные данные val"
    
    if val < val_min:
        print(msg_sec)
    elif val > val_min - 1 and val < val_hour:
        print(msg_min)
    elif val > val_hour - 1 and val < val_day:
        print(msg_hour)
    elif val > val_day - 1 and val < val_year:
        print(msg_day)
    elif val > val_year:
        print(msg_year)
    else:
        print(msg_else)

def to_cube(add17):
    cubes = []
    cubes_div7 = []
    for val1 in range(1,1000):
        val1 += add17 
        if (val1%2):
            cubes.append( pow(val1,3) )
    for val in cubes[0:10]:
        print("val=",val)

# признак делимости на 7 - неправильный как в методичке            
#    for val2 in cubes[0:10]:
#        val_str = str(val2)
#        val_sum = 0
#        for letter in val_str:
#            val_sum += int(letter)
#        print("val_str = ", val_str, ", sum=", val_sum, " div7=", val_sum % 7, "val_div7 = ", val2%7)
#        if val_sum % 7.0 == 0:
#            cubes_div7.append(val2)
#    for val in cubes_div7[0:10]:
#        print("val_div7=",val)

    for val2 in cubes:
       if val2 in [27]:
           cubes_div7.append(val2)
       # правило работает для 3-х значных чмчел и выше
       if val2 < 100: continue 
       
       val_str = str(val2)
       part1 = ""
       #print("val_str = ", val_str)
       for letter in val_str[0:-1]:
           part1 += letter
       part2 = val_str[-1]
       part1 = int(part1)
       part2 = int(part2)
       #print(part1, part2)
       if part1 < part2:
           val1 = part1*2
           negative_result = (part2 - val1)%7
       elif part1 > part2:
           val1 = part2*2
           negative_result = (part1 - val1)%7
       else:
           print("Немогу посчитать! Проверьте входные данные для val_str= ", val_str)
           
       if not negative_result: 
           cubes_div7.append(val_str)
           
    for val in cubes_div7[0:10]:
        print("val_div7 = ", val)
       
    return len(cubes_div7)

def declination_procents(val):
    if not val: exit
    vals = range(1, val+1)
    value_procents = []
    add_str = ""
    for value in vals:
        str_value = str(value)
        if ( int(str_value) > 9 and int(str_value) < 20) :
            print ("val = ", len(str_value), str_value[0])
            value_procents.append(str(value) + " процентов")
        else:
            num = int( str_value[-1] )
            if num == 1:
                add_str = " процент"
            elif num == 2:
                add_str = " процента" 
            elif num == 3:
                add_str = " процента"
            elif num == 4:
                add_str = " процента"
            elif num == 5:
                add_str = " процентов"
            elif num == 6:
                add_str = " процентов"
            elif num == 7:
                add_str = " процентов"
            elif num == 8:
                add_str = " процентов"  
            elif num == 9: 
                add_str = " процентов"
            elif num == 0:
                add_str = " процентов"
            else:
                print("Ошибка вычисления в num")
            value_procents.append(str(value) + add_str)
        
    for each in value_procents:
        print(each)
    
if __name__ == "__main__":
    main()
    
