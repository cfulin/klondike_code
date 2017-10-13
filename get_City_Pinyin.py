#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from pypinyin import lazy_pinyin
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def city_Pinyin(data):
    pinyin_first = []
    pinyin_last = []
    datas = list(data.values)
    for cityName in datas:
        city = str(cityName[0])
        getPinyin = (lazy_pinyin((unicode(city))))
        pinyin_first.append(str(getPinyin[0]))
        pinyin_last.append(str(getPinyin[-1]))
    pinyin_first = pd.DataFrame(pinyin_first, columns=['pinyin_first'])
    pinyin_last = pd.DataFrame(pinyin_last, columns=['pinyin_last'])
    data = pd.concat([data, pinyin_first, pinyin_last], axis=1)
    data.to_excel("city_dealcity_pinyin.xlsx")
    # return data


def main():
    data = pd.read_excel("city_dealcity.xlsx")
    city_Pinyin(data)


if __name__ == '__main__':
    main()
