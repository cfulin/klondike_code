#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import json
import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import demjson
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_one_page(url):
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
    try:
        response = requests.get(url, headers)
        if response.status_code == 200:
            response = response.text
            return response
        else:
            return None
    except RequestException:
        return None


def write_to_file(content):
    # contents = {}
    # contents.update(content)
    # contents.update({"contributors": "cfl"})
    # dict(content, **{"contributors": "cfl"})
    with codecs.open('city.txt', 'a') as f:
        # f.write(json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')) + ",")
        # f.write(json.dumps(content, ensure_ascii=False) + "\n")
        f.write(content + "\n")
        f.close()


def parse_one_page(html):
    # <span style="FONT-SIZE: 15pt; FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'">
    # 个）：太原市、大同市、朔州市、忻州市、阳泉市、晋中市、吕梁市、长治市、临汾市、晋城市、运城市</span>
    # pattern = re.compile('<p.*?class="MsoNormal".*?'
    #                      + '<span.*?style="FONT-SIZE:.*?15pt.*?>(.*?)</span>', re.S)
    pattern = re.compile(u'(?is)<td>(.*?)\n.*?</td>', re.S)
    # pattern = re.compile('(?<=<td>).*(?=</td>)')
    # pattern = re.compile(u'<table.*?class="maintext".*?width="500".*?border="0">.*?'
    #                      + u'<tr>.*?省(.*?)市.*?', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield item
    # soup = BeautifulSoup(html)
    # print soup.tr


def main():
    # url = 'http://maoyan.com/board/4?offset=' + str(offset)
    # url = 'http://www.360doc.com/content/12/0601/21/6818730_215294560.shtml'
    # url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/13.html'
    # url = 'http://data.acmr.com.cn/member/city/city_md.asp'
    # html = get_one_page(url)
    with codecs.open('city.html', 'r') as f:
        html = f.read()

    # soup = BeautifulSoup(html, "lxml")
    # print soup.prettify()
    # print soup.tr.contents
    # print soup.select(".maintext")
    # print soup.find_all(text=re.compile(u'((?=河南省)((?!市)[^<])*(?=市))'))
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    main()
