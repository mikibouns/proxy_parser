import requests
from lxml import html
from proxies_list import ProxyList # импортируем клас из локального файла



class ParserProxy:

    def __init__(self, proxy_list, currency_pair='ETH_USD'):
        self.currency_pair = currency_pair
        self.URL = 'https://exmo.me/ru/trade#?pair=BTC_USD' # ссылка на парсируемый сайт
        self.proxy_list = proxy_list
        self.proxy = {
            'http': self.proxy_list.get_proxy(),
            }
        print(self.proxy_list.get_proxy()) # выводим на экран результат работы метода get_proxy()

    def get_rate(self):
        # получаем целевую страницу html используя прокси сервер
        parsed_body = html.fromstring(requests.get(self.URL, proxies=self.proxy).text)
        # получаем значение обходя дерево html через метод xpath
        rate_pc = parsed_body.xpath("//div/ul/li[@pair='%s']/div[4]/text()" % self.currency_pair)
        return rate_cp


if __name__ == '__main__':
    proxy_list = ProxyList() # создаем экземпляр класса ProxyList
    par_prox = ParserProxy(proxy_list, 'ETH_USD')
    rate_ETH_USD = par_prox.get_rate()
    print(float(rate_ETH_USD[0]))