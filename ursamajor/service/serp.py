import requests
from bs4 import BeautifulSoup
from config.settings import DEBUG

__all__ = ['seprprocess']

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) " \
                    "Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent": USER_AGENT}

query = "beidou"
query = query.replace(' ', '+')
GOOLE_URL = "https://google.com/search?q={}&gl=us&hl=en&start=60".format(query)


def seprprocess():
    content = query()
    result = parse(content=content)
    return result


def query() -> str:
    if DEBUG:
        # response = requests.get(GOOLE_URL, headers=headers)
        z = open('query.txt', 'r')
        return z.read()
    else:
        response = requests.get(GOOLE_URL, headers=headers)

    if response and response.status_code == 200:
        return response.content
    else:
        return ''


def parse(content: str) -> list:
    results = list()

    if content and len(content):
        soup = BeautifulSoup(content, "lxml")
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
    return results
