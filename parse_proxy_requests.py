import requests
from lxml import html

URL = 'https://exmo.me/ru/trade#?pair=BTC_USD'

proxy = {
    'http':'52.17.165.9:3130',

}

# Преобразование тела документа в дерево элементов (DOM)
parsed_body = html.fromstring(requests.get(URL, proxies=proxy).text)
rate_ETH_USD = parsed_body.xpath("//div/ul/li[@pair='ETH_USD']/div[4]/text()")

print(float(rate_ETH_USD[0]))
# Выполнение xpath в дереве элементов
# print parsed_body.xpath('//title/text()') # Получить title страницы
# print parsed_body.xpath('//a/@href') # Получить аттрибут href для всех ссылок