import requests
from lxml import html
from proxies_list import ProxyList # импортируем клас из локального файла

URL = 'https://exmo.me/ru/trade#?pair=BTC_USD'# ссылка на парсируемый сайт

proxy_list = ProxyList() # создаем экземпляр класса ProxyList
print(proxy_list.get_proxy()) # выводим на экран результат работы метода get_proxy()

proxy = {
    'http': proxy_list.get_proxy(),
}
# получаем целевую страницу html используя прокси сервер
parsed_body = html.fromstring(requests.get(URL, proxies=proxy).text)
# получаем значение обходя дерево html через метод xpath
rate_ETH_USD = parsed_body.xpath("//div/ul/li[@pair='ETH_USD']/div[4]/text()")

print(float(rate_ETH_USD[0]))