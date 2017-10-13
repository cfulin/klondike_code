#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_data_length(data):
    data_length = len(data.values)
    return data_length


def city_Analyse(data):
    data_pinyin_first = list(data['pinyin_first'])
    data_pinyin_last = list(data['pinyin_last'])
    data_list = list(data.values)
    return data_pinyin_first, data_pinyin_last, data_list


def pinyin_Match(data_pinyin_first, data_pinyin_last, data_list, data):
    data_length = get_data_length(data)
    ranNum = random.randint(0, data_length)
    result = data_list[ranNum][0]

    while ranNum < data_length - 1:
        for flag in range(data_length):
            if str(data_pinyin_last[ranNum]) == str(data_pinyin_first[flag]):
                result = result + " => " + data_list[flag][0]
                ranNum = flag
                break
            elif flag == data_length - 1:
                city_Name = data_list[ranNum][0]
                ranNum = data_length - 1
                print result
                print "无法匹配: " + city_Name + " 接龙游戏中断"


def main():
    data = pd.read_excel("city1_dealcity_pinyin.xlsx")
    data_pinyin_first, data_pinyin_last, data_list = city_Analyse(data)
    pinyin_Match(data_pinyin_first, data_pinyin_last, data_list, data)


if __name__ == '__main__':
    main()
