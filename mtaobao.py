# -*- coding:utf-8 -*-

#try:
#    from http.cookiejar import CookieJar
#except ImportError:
#    from cookielib import CookieJar

from download import download, download_item
import lxml.html
import urllib.request
import json


url = 'https://www.taobao.com/markets/tbhome/market-list'
cat_xpath = '/html/body/div[3]/div/div/div/div/div/div/ul/li/a'
detail_xpath = '/html/body/div[3]/div/div/div/div/div/div/ul/li/div/a'

tree = lxml.html.fromstring(download(url))

datas_cat = tree.xpath(cat_xpath)
datas_detial = tree.xpath(detail_xpath)

for cat in datas_cat[2:]:
    print(cat.text_content())

a = []
for det in datas_detial:
    a.append(len(det.text_content()))

print(sum(a))

#url = 'https://s.m.taobao.com/search?q=%E6%89%8B%E6%9C%BA&search=Submit&tab=all&page=20'

#html = download(nvzhuang)
#with open("1", 'w') as f:
#    print(html.decode('utf-8'), file=f)

#cj = CookieJar()
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#res = opener.open(nvzhuang)
#print(cj)
#for i in cj:
#    print(i.name, i.value)

#print(res.read())

#data = json.loads(download(url).decode('utf-8'))

#total_results = data['totalResults']
#total_page = data['totalPage']
#
#for item in data['itemsArray']:
#    print(item['title'])












