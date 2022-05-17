#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:02:26 2022
Михаил Рашев ДЗ 4.
Работа с модулями и пакетами
@author: rashev
"""

import requests as rq
import xml.etree.ElementTree as ET
import decimal as dec
from datetime import datetime as dt
import sys

import utils.mikhail_rashev_dz4_module as mymod


def main(vals_in):

    print("ДЗ 4.2.\n")
    # 1
    print("Можно использовать формат Decimal, для более короткого\
 и наглядного представления числа\n")
    currency1 = "EUR"
    value1 = currency_rates(currency1)
    print(f"currency {currency1}, value {value1}")
    # 2
    currency = "eur"
    currency2 = currency.upper()
    value2 = currency_rates(currency2)
    print(f"currency {currency}, value {value2}")
    # 3
    currency = "usd"
    currency3 = currency.upper()
    value3 = currency_rates(currency3)
    print(f"currency {currency}, value {value3}")
    # 4 string methods
    currency = "usd"
    currency4 = currency.upper()
    value4 = currency_rates_str(currency4)
    print(f"Only str methods, currency {currency}, value {value4}\n")
    #
    print("ДЗ 4.3.\n")
    print("Возвравщать дату мз функции удобнее в формате datetime,\
так как потом её удобнее использовать в дальнейших вычисление, а перев выводом\
её можно быстро перевести в строку.\n")
    currency = "usd"
    currency5 = currency.upper()
    value5, cbr_date = currency_rates_date(currency5)
    print(f"Only str methods, currency {currency}, value {value5}, \
date в формате date {cbr_date}\n")
    #
    print("ДЗ 4.4.\n")
    currency = "usd"
    currency6 = currency.upper()
    value6 = mymod.currency_rates(currency6)
    print(f"модуль utils, currency {currency}, value {value6}\n")
    value6 = mymod.currency_rates_str(currency6)
    print(f"модуль utils, str methods, currency {currency}, value {value6}\n")
    value6, cbr_date = mymod.currency_rates_date(currency6)
    print(f"модуль utils, currency {currency}, value {value6}, \
date в формате date {cbr_date}\n")
    #
    print("ДЗ 4.5.\n")
    if len(vals_in) > 0:
        word = "есть"
        for val in vals_in:
            value7, cbr_date = currency_rates_date(val.upper())
            print(f"внешние аргументы - {word}, currency {val}, value \
{value7}, date в формате date {cbr_date}\n")
    else:
        word = "нет"
        currency7 = "RUB"
        value7, cbr_date = currency_rates_date(currency7.upper())
        print(f"внешние аргументы - {word}, currency {currency7}, \
value {value7}, date в формате date {cbr_date}\n")


def currency_rates(char_code):
    path = "http://www.cbr.ru/scripts/XML_daily.asp"
    results = rq.get(path)
    print(f"статус запроса ЦБР - {results.status_code}")
    # print(results.text)

    # ret_value= float()
    ret_value = dec.Decimal()
    mytree = ET.fromstring(results.content)

    all_char_codes = [x[1].text for x in mytree]
    if char_code not in all_char_codes:
        return None

    for child in mytree:
        if child[1].text == char_code:
            # ret_value = float( child[4].text.replace(",", ".") )
            dec.getcontext().prec = 4
            ret_value = dec.Decimal(child[4].text.replace(",", "."))

    return ret_value


def currency_rates_str(char_code):
    path = "http://www.cbr.ru/scripts/XML_daily.asp"
    results = rq.get(path)
    print(f"статус запроса ЦБР - {results.status_code}")
    if char_code not in results.text:
        return None
    ret_value = dec.Decimal()
    content = results.text.split("Valute ID")

    for strg in content:
        num1 = strg.find(char_code)
        num2 = strg.find("Value")
        if num1 != -1:
            val = strg[num2+6:num2+13]
            ret_value = dec.Decimal(val.replace(",", "."))

    return ret_value


def currency_rates_date(char_code):
    path = "http://www.cbr.ru/scripts/XML_daily.asp"
    results = rq.get(path)
    print(f"статус запроса ЦБР - {results.status_code}")
    # print(results.text)

    # ret_value= float()
    ret_value = dec.Decimal()
    mytree = ET.fromstring(results.content)

    all_char_codes = [x[1].text for x in mytree]

    for child in mytree:
        if child[1].text == char_code:
            # ret_value = float( child[4].text.replace(",", ".") )
            dec.getcontext().prec = 4
            ret_value = dec.Decimal(child[4].text.replace(",", "."))

    elem = ET.fromstring(results.text)
    date_time_str = elem.attrib.get('Date').replace(".", "/")
    cbr_date = dt.strptime(date_time_str, '%d/%m/%Y')

    if char_code not in all_char_codes:
        print(None, cbr_date)
        return (None, cbr_date)
    else:
        return (ret_value, cbr_date)


if __name__ == "__main__":
    main(sys.argv[1:])
