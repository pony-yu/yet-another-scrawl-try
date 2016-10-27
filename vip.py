# -*- coding:utf-8 -*-

import lxml.html
import time
from download import download, download_item
import json

#
# get all links
#
url = 'http://category.vip.com/ajax/getCategory.php?callback=getCategory&tree_id=117'
html = download(url)

str_links = html.decode('utf-8')[12:-1]       # getCategory({*})
datas = json.loads(str_links)['data']

vip_links = []
for data in datas:
    print("Get", data['cate_name'])
    vip_links.append('http://category.vip.com/' + data['url'])

print(vip_links)

##
## TEST
##
#url_items = vip_links[0]
url_items = 'http://category.vip.com/search-3-0-1.html?q=1|30074|'
#with open('1.html', 'w') as f:
#    print(download(url_items).decode('utf-8'), file=f)

tree = lxml.html.fromstring(download(url_items))
xpath = '//*[@id="J_searchCatList"]/div/div/h4/a'

titles = tree.xpath(xpath)

with open('1', 'w') as f:
    for t in titles:
        print(t.attrib['title'], file=f)



















