# -*- coding:utf-8 -*-

import lxml.html
import time
from download import download, download_item

#
# first catgory
#
url = 'https://www.tmall.com/'
html = download(url)
tree = lxml.html.fromstring(html)

xpath = '//*[@id="content"]/div[2]/div[1]/div[3]/div/ul/li/a'
tmall_links = tree.xpath(xpath)


#
# second tmall nvzhuang
#
nvzhaung = tmall_links[0].attrib['href']

tmall_nvzhuang_url = 'https:' + nvzhaung
tmall_nvzhuang_xpath = '//*[@id="J_TmFushiNavCate"]/ul/li/ul/li/a'

nvzhuang_html = download(tmall_nvzhuang_url)
tree = lxml.html.fromstring(nvzhuang_html)

# get the links
links = tree.xpath(tmall_nvzhuang_xpath)
for link in links:
    ln = link.attrib['href']
    #print(ln)
    download_item(ln, "tmall.txt", max_page=50)
    #print(link.text_content())
    break





