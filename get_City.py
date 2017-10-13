#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("gbk")


def read_cityfile():
    # 打开文件
    inpath = 'city.txt'
    outpath = inpath.split('.')[0] + '_outfile' + '.xlsx'
    # outpath = unicode('outfile.xlsx', 'utf-8')
    return inpath, outpath


def get_City(inpath):
    cityData = []
    data = open(inpath, 'r')
    while True:
        line = data.readline()
        if line:
            cityData.append(line)
        else:
            break
    data.close()
    return cityData


# def flatten(nested):
#     try:
#         try: nested + ''
#         except TypeError: pass
#         else: raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):
#                 yield element
#     except TypeError:
#         yield nested


def data_Process(data):
    flag = 0
    for cityName in data:
        citys = str(cityName).replace(u'黑龙江', "").replace(u'吉林省', "").replace(u'辽宁', "")\
            .replace(u'新疆', "").replace(u'内蒙', "") .replace(u'西藏', "").replace(u'青海', "") \
            .replace(u'甘肃', "").replace(u'宁夏', "").replace(u'陕西', "").replace(u'山西', "")\
            .replace(u'河北', "").replace(u'河南', "").replace(u'山东', "").replace(u'安徽', "")\
            .replace(u'江苏', "").replace(u'湖北', "").replace(u'湖南', "").replace(u'四川', "")\
            .replace(u'云南', "").replace(u'贵州', "").replace(u'江西', "").replace(u'浙江', "")\
            .replace(u'福建', "").replace(u'广西', "").replace(u'广东', "").replace(u'台湾', "") \
            .replace(u'海南', "").replace(u'重庆', "").replace(u'省', "").replace(u'市', "")\
            .replace(u'\n', "").replace(' ', "")

        data[flag] = citys
        flag += 1
    data = list(set(data))
    data = pd.DataFrame(data, columns=['city'])

    # none_vin = (data['city'].isnull()) | (data['city'].apply(lambda x: str(x).isspace()))
    # data_not_null = data[~none_vin]  # 去除空格
    # data_not_null = pd.DataFrame(data_not_null[3:], index=[range(len(data_not_null))])

    data = data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    data = data.drop_duplicates(["city"])  # 去除重复行
    data = data[1:].reset_index(drop=True)
    data.to_excel("city_dealcity.xlsx")
    print("City data has been got successful!")


def main():
    inpath, outpath = read_cityfile()
    cityData = get_City(inpath)
    data_Process(cityData[6:])
    # flatCity = flatten(cityData)
    cityData = pd.DataFrame(cityData[6:], columns=['city'])
    cityData.to_excel(outpath)


if __name__ == '__main__':
    main()
