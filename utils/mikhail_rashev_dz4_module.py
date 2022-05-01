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
    if char_code not in all_char_codes:
        return None

    for child in mytree:
        if child[1].text == char_code:
            # ret_value = float( child[4].text.replace(",", ".") )
            dec.getcontext().prec = 4
            ret_value = dec.Decimal(child[4].text.replace(",", "."))

    elem = ET.fromstring(results.text)
    date_time_str = elem.attrib.get('Date').replace(".", "/")
    cbr_date = dt.strptime(date_time_str, '%d/%m/%Y')

    if char_code not in all_char_codes:
        return (None, cbr_date)
    else:
        return (ret_value, cbr_date)
