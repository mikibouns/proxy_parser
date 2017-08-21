import requests
from urllib.request import urlopen
from urllib.parse import urljoin
from lxml.html import fromstring

URL = 'https://exmo.me/ru/trade#?pair=BTC_USD'
ITEM_PATH = '.graph_indexes_top .pair_item'
VALUE_PATH = '.graph_indexes_top .pair_price'

def parse_rate(html):
    f = urlopen(html).read().decode('utf-8')# получаем html страницу в читаемом формате с кодировкой utf-8
    list_doc = fromstring(f)# создаем дерево элементов с помощью функции fromstring
    vp = list_doc.cssselect(VALUE_PATH)# выборка из дерева по class
    ip = list_doc.cssselect(ITEM_PATH)
    currency_pair = [elem.cssselect('div')[0].text for elem in ip]# генерируем список валютных пар
    rate = [elem.cssselect('div')[0].text for elem in vp]# генерируем список курсов
    print(currency_pair)
    print(rate)



def main():
    parse_rate(URL)

if __name__ == '__main__':
    main()