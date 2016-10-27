# -*- coding:utf-8 -*-

import lxml.html
#import time
from download import download, download_item
import json


#
# get all links
#
url = 'https://www.jd.com/allSort.aspx'
xpath = '/html/body/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/dl/dd/a'
html = download(url)
tree = lxml.html.fromstring(html)


jd_links = tree.xpath(xpath)

#with open('jd', 'w') as f:
#    for ln in jd_links:
#        print(ln.attrib['href'], file=f)


## TEST
##//list.jd.com/list.html?cat=1713,4855,4870

products = 'http:' + jd_links[10].attrib['href']
pro_tree = lxml.html.fromstring(download(products))

#
# get total pages
#
total_pages_xpath = '//*[@id="J_bottomPage"]/span[2]/em[1]/b'
total_pages = pro_tree.xpath(total_pages_xpath)
print(total_pages[0].text_content())

#
# get product name and skuid
#
name_xpath = '//*[@id="plist"]/ul/li[1]/div/div[3]/a/em'
name = pro_tree.xpath(name_xpath)[0].text_content()
print(name)
skuid_xpath = '//*[@id="plist"]/ul/li[1]/div'
skuid = pro_tree.xpath(skuid_xpath)[0].attrib['data-sku']
print(skuid)

#
# get price
#
json_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + skuid
# json: [{"id":"J_19637836","p":"122.40","m":"132.80","op":"122.40"}]
json_price = json.loads(download(json_url).decode('utf-8'))[0]
print(json_price['p'])





