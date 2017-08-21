import requests
from lxml.html import fromstring


url_site = 'https://exmo.me/ru/trade#?pair=BTC_USD'
proxy_url = 'https://www.ip-adress.com/proxy_list/' #

def get_proxy_list(proxy_url):
    str = fromstring((requests.get(proxy_url)).content)
    ports = str.xpath("//table/tbody/tr/td[1]/text()")
    ipaddresses = str.xpath("//table/tbody/tr/td[1]/a/text()")
    proxy_list = [ipaddresses[i] + ports[i] for i in range(len(ipaddresses))]
    return proxy_list

def give_proxy(proxy_list, url_site):
    for proxy in proxy_list:
        url = 'http://' + proxy
        try:
            r = requests.get(url_site, proxies={'http':url})
            if r.status_code == 200:
                return url
        except requests.exceptions.ConnectionError:
            print('error')
            continue



proxy_list = get_proxy_list(proxy_url)
result = give_proxy(proxy_list, url_site)
print(result)