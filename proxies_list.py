import requests
from lxml.html import fromstring


class ProxyList:
    url_site = 'https://exmo.me/ru/trade#?pair=BTC_USD'
    proxy_url = 'https://www.ip-adress.com/proxy_list/'

    def __init__(self):
        str = fromstring((requests.get(self.proxy_url)).content)
        ports = str.xpath("//table/tbody/tr/td[1]/text()")
        ipaddresses = str.xpath("//table/tbody/tr/td[1]/a/text()")
        self.proxy_list = [ipaddresses[i] + ports[i] for i in range(len(ipaddresses))]

    def get_proxy(self):
        for proxy in self.proxy_list:
            url = proxy
            try:
                r = requests.get(self.url_site, proxies={'http': url})
                if r.status_code == 200:
                    return url
            except requests.exceptions.ConnectionError:
                continue


if __name__ == '__main__':
    proxy = ProxyList()
    print(proxy.get_proxy())