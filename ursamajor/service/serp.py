from pprint import pprint

import requests
from bs4 import BeautifulSoup

__all__ = ['seprprocess']

# https://searchengines.guru/showthread.php?t=1014147
from config.settings import DEBUG

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) " \
                    "Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "beidou"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}&gl=us&hl=en&start=10"

headers = {"user-agent": USER_AGENT}
proxies = {
    # 'https': '163.204.247.167:9999',
    # 'https': '205.158.57.2:53281',
    # 'http': '',
}


def seprprocess():
    content = query()
    result = parse(content=content)
    return result


def query() -> str:
    if DEBUG:
        return open('query.txt', 'r')  # открыть файл из рабочей директории в режиме чтения
    else:
        response = requests.get(URL, headers=headers)

    # for proxy in proxies:
    #     response = requests.get(URL, headers=headers, proxies=proxies)
    #     if response.status_code == requests.codes['ok']:
    #         break
    #
    #     response.text

        if response.status_code == 200:
            # print(response.content)
            return response.content
        else:
            return ''


def parse(content: str) -> list:
    soup = BeautifulSoup(content, "lxml")
    results = list()
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)

    # pprint(results)
    return results
