#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def read_cityfile():
    # 打开文件
    inpath = 'city.json'
    outpath = inpath.split('.')[0] + '_outfile' + '.xlsx'
    # outpath = unicode('outfile.xlsx', 'utf-8')
    return inpath, outpath


def getCity(inpath):
    with open(inpath, 'r') as f:
        data = json.load(f)
    gLen = len(data['data'])
    city = []
    for i in range(gLen):
        city.append(data['data'][i]['c'])
    return city


def flatten(nested):
    try:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


def dataProcess(data):
    data = list(data.values)
    flag = 0
    for cityName in data:
        citys = str(cityName[0]).replace(u'市', "").replace(u'自治州', "").replace(u'哈萨克', "").replace(u'盟', "")\
            .replace(u'土家族', "").replace(u'苗族', "").replace(u'藏族', "").replace(u'蒙古族', "")\
            .replace(u'羌族', "").replace(u'彝族', "").replace(u'傣族', "").replace(u'回族', "") \
            .replace(u'朝鲜族', "").replace(u'布依族', "") .replace(u'侗族', "").replace(u'哈尼族', "") \
            .replace(u'白族', "").replace(u'景颇族', "") .replace(u'傈僳族', "").replace(u'蒙古', "") \
            .replace(u'壮族', "").replace(u'地区', "")
        data[flag][0] = citys
        flag += 1
    data = pd.DataFrame(data, columns=['city'])

    data = data.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
    data = data.drop_duplicates()  # 去除重复行
    none_vin = (data['city'].isnull()) | (data['city'].apply(lambda x: str(x).isspace()))
    data_not_null = data[~none_vin]  # 去除空格

    data_not_null.to_excel("city1_dealcity.xlsx")
    print data_not_null
    print("City data has been got successful!")


def main():
    inpath, outpath = read_cityfile()
    cityData = getCity(inpath)
    flatCity = flatten(cityData)
    cityData = pd.DataFrame(flatCity, columns=['city'])
    cityData.to_excel(outpath)
    dataProcess(cityData)


if __name__ == '__main__':
    main()
