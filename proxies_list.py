import requests
from lxml.html import fromstring

class ProxyList:
    url_site = 'https://exmo.me/ru/trade#?pair=BTC_USD' # ссылка на целевой сайт
    proxy_url = 'https://www.ip-adress.com/proxy_list/' # ссылка на список прокси серверов

    def __init__(self):
        str = fromstring((requests.get(self.proxy_url)).content) # получаем форматированный html
        # с помощью xpath переходим по дереву html, вынимаем имя порта
        ports = str.xpath("//table/tbody/tr/td[1]/text()")
        # с помощью xpath переходим по дереву html, вынимаем адрес сервера
        ipaddresses = str.xpath("//table/tbody/tr/td[1]/a/text()")
        # с помощью генератора списка создаем список ip адрес + порт
        self.proxy_list = [ipaddresses[i] + ports[i] for i in range(len(ipaddresses))]

    def get_proxy(self):
        # выполняем обход списка proxy_list
        for proxy in self.proxy_list:
            # если request.get возвращает код 200 возвращаем значение
            try:
                r = requests.get(self.url_site, proxies={'http': proxy})
                if r.status_code == 200:
                    return proxy
            # если request.get не возвращает код 200 переходим к следующей итерации
            except requests.exceptions.ConnectionError:
                continue


if __name__ == '__main__':
    proxy = ProxyList()
    print(proxy.get_proxy())