import requests as requests

from newspaper import Article

from ursamajor.models import Page
from ursamajor.service.exceptions import contains

TIMEOUT = 10


def links_process(links: list):
    for raw_link in links:
        link = raw_link['link'].strip()

        if not contains(link) and not is_exist_in_db(link):
            result = requests.get(url=link, timeout=TIMEOUT)
            article = fetch_main_content(result.content)
            save_page(link=link, html=result.content, article=article)


def fetch_main_content(html: str) -> Article:
    a = Article(url='')
    a.html = html
    a.download_state = 2
    a.parse()
    return a


def save_page(link: str, html: str, article: Article):
    p = Page()
    p.layout = p.LAYOUT_PAGE
    p.url = link
    p.raw_html = html
    p.raw_content = article.text.strip()
    p.name = article.title

    p.save()


def is_exist_in_db(link: str) -> bool:
    try:
        Page.objects.get(url=link)
        return True
    except Page.DoesNotExist:
        return False
