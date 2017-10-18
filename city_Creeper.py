#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_one_page(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        return response.read()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason


def save_html(file_name, file_content):
    with open("data" + file_name.replace('/', '_') + ".html", "wb") as f:
        f.write(file_content)


def file_is_not(filename):
    return os.path.exists(filename)


def write_to_file(content):
    # contents = {}
    # contents.update(content)
    # contents.update({"contributors": "cfl"})
    # dict(content, **{"contributors": "cfl"})
    with codecs.open('data/city.txt', 'a') as f:
        # f.write(json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')) + ",")
        # f.write(json.dumps(content, ensure_ascii=False) + "\n")
        f.write(content + "\n")
        f.close()


def parse_one_page(html):
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
    # url = 'http://www.360doc.com/content/12/0601/21/6818730_215294560.shtml'
    # url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/13.html'
    file = file_is_not('data/city.html')
    if file:
        with codecs.open('data/city.html', 'r') as f:
            html = f.read()
    else:
        url = 'http://data.acmr.com.cn/member/city/city_md.asp'
        html = get_one_page(url)
        save_html("city", html)

    # soup = BeautifulSoup(html, "lxml")
    # print soup.prettify()
    # print soup.tr.contents
    # print soup.select(".maintext")
    # print soup.find_all(text=re.compile(u'((?=河南省)((?!市)[^<])*(?=市))'))
    if html > 0:
        for item in parse_one_page(html):
            write_to_file(item)

if __name__ == '__main__':
    main()
