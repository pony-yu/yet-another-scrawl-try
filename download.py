# -*- coding:utf-8 -*-

import urllib.request, urllib.error
import ijson

import time
# test
import lxml.html
#


class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """
    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
        if sleep_secs > 0:
            time.sleep(sleep_secs)

        self.domains[domain] = datetime.now()


#
# TODO: proxy, header...
#
def download(url, num_retries=2):
    """Crawling the category of ...
    """
    print("Downloading: %s..." % url)
    try:
        html = urllib.request.urlopen(url).read()  # .read().decode('utf-8')
    except urllib.error.URLError as e:
        print("Downloading error: ", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)

    print("Download completed.")
    return html


def download_item(url, filename='data.txt', *, num_retries=2, max_page=300, \
        page_size=20, page_no=1, proxy=None):
    """Get items
    """

    if page_no > max_page:
        return

    # check, only one '?'
    if url.count('?') != 1:
        print("Can't use this way, set url to None...")
        url = ''

    hd, tl = url.split('?')
    head = 'https://list.tmall.com/m/search_items.htm?page_size=%d&page_no=%d&' % (page_size, page_no)
    url_req = head + tl

    print('Downloading %s...' % url_req)
    try:
        html_response = urllib.request.urlopen(url_req)  # .read().decode('utf-8')
    except urllib.error.URLError as e:
        print("Downloading error: ", e.reason)
        html_response = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download_item(url, filename, num_retries=num_retries-1,\
                        max_page=max_page, page_size=page_size, page_no=page_no, proxy=proxy)
    print('Request done...')
    #json_html = json.loads(download(""))

    objects = ijson.items(html_response, 'item.item')

    # TODO check Generator empty ??
    #if not list(objects):
    #    return

    items = (o for o in objects if o['item_id'])   # can set filter
    with open(filename, "a+") as f:
        for item in items:
            item_id = item['item_id']
            price = item['price']
            title = item['title']
            print(item_id, title, price, sep=",", file=f)

    # TODO delay
    if page_no % 10 == 0:
        time.sleep(2)

    return download_item(url, filename, num_retries=num_retries, max_page=max_page, \
            page_size=page_size, page_no=page_no+1, proxy=proxy)


    #print(list(item))
    #with open("1.json", "w") as f:
    #    print(json_html['item'], file=f)

if __name__ == '__main__':
    #protocol = 'https:'
    #resource = None
    url = 'https://www.tmall.com/'
    html = download(url)
    tree = lxml.html.fromstring(html)

    ##tmall_select = 'div.category-tab-pannel > ul > li > a'
    ##links = tree.cssselect(tmall_select)
    ##print(links[0].text_content())

    # get the links
    tmall_xpath = '//*[@id="content"]/div[2]/div[1]/div[3]/div/ul/li/a'
    links = tree.xpath(tmall_xpath)
    ##print(links[0].attrib['href'])
    #for link in links:
    #    print(link.attrib['href'])

    #
    # sub category
    #
    #tmall_nvzhuang_xpath = '//*[@id="J_TmFushiNavCate"]/ul/li/a'
    tmall_nvzhuang_xpath = '//*[@id="J_TmFushiNavCate"]/ul/li[1]/ul/li[1]/a'

    tmall_nvzhuang_url = 'https:' + links[0].attrib['href']
    sub_html = download(tmall_nvzhuang_url)

    with open('1.html', 'w') as f:
        print(sub_html.decode('utf-8'), file=f)

    sub_tree = lxml.html.fromstring(sub_html.decode('utf-8'))
    sub_links = tree.xpath(tmall_nvzhuang_xpath)

    print(sub_links)

    #for link in sub_links:
    #    print(link.attrib['href'])

    #with open("2.html", "w") as f:
    #    print(html.decode('utf-8'), file=f)

