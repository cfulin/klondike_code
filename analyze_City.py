#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from pypinyin import lazy_pinyin
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_data_length(data):
    data_length = len(data.values)
    return data_length


def city_analyse(data):
    data_pinyin_first = list(data['pinyin_first'])
    data_pinyin_last = list(data['pinyin_last'])
    data_city_list = list(data['city'])
    return data_pinyin_first, data_pinyin_last, data_city_list


def pinyin_match(data_pinyin_first, data_pinyin_last, data_city_list, data):
    data_length = get_data_length(data)
    city_is_right = False
    result = raw_input("请输入第一个城市名：")
    for i in range(len(data_city_list)):
        if result == data_city_list[i]:
            city_is_right = True
            num = i
            break

    if city_is_right:
        cityPinyin = lazy_pinyin(unicode(result))
        data_pinyin_temp = cityPinyin[-1]
        while num < data_length - 1:
            for flag in range(data_length):
                if data_pinyin_temp == data_pinyin_first[flag]:
                    result = result + " => " + data_city_list[flag]
                    num = flag
                    data_pinyin_temp = data_pinyin_last[num]
                    break
                elif flag == data_length - 1:
                    city_Name = data_city_list[num]
                    num = data_length - 1
                    print result
                    print "无法匹配: " + city_Name + ",接龙游戏中断"
    else:
        print "请输入正确的城市名称！"
        pinyin_match(data_pinyin_first, data_pinyin_last, data_city_list, data)


def main():
    data = pd.read_excel("data/city_dealcity_pinyin.xlsx")
    data_pinyin_first, data_pinyin_last, data_city_list = city_analyse(data)
    pinyin_match(data_pinyin_first, data_pinyin_last, data_city_list, data)


if __name__ == '__main__':
    main()
