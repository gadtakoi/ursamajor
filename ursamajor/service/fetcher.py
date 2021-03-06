import requests as requests
from django.utils.text import slugify

from newspaper import Article

from ursamajor.models import Page
from ursamajor.models.layout import Layouts
from ursamajor.service.exceptions import contains

TIMEOUT = 10


def links_process(links: list):
    for raw_link in links:
        link = raw_link['link'].strip()

        if not contains(link) and not is_exist_in_db(link):
            try:
                result = requests.get(url=link, timeout=TIMEOUT)
                article = fetch_main_content(result.content)
                save_page(link=link, html=result.content, article=article)
            except (requests.exceptions.ConnectTimeout, requests.exceptions.SSLError) as e:
                pass


def fetch_main_content(html: str) -> Article:
    a = Article(url='')
    a.html = html
    a.download_state = 2
    a.parse()
    return a


def save_page(link: str, html: str, article: Article):
    p = Page()
    p.layout = Layouts.LAYOUT_PAGE
    p.slug = slugify(article.title)[:50]
    p.url = p.slug
    p.parent = get_section()
    p.source_url = link
    p.raw_html = html
    p.raw_content = article.text.strip()
    p.name = article.title
    p.save()
    p.url = p.build_url()
    p.save()


def get_section():
    return Page.publicated.filter(layout=Layouts.LAYOUT_SECTION).first()


def is_exist_in_db(link: str) -> bool:
    try:
        Page.objects.get(source_url=link)
        return True
    except Page.DoesNotExist:
        return False
