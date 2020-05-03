import aiohttp
import asyncio

import requests as requests
from django.db import IntegrityError
from django.utils.text import slugify

from newspaper import Article

from ursamajor.models import Page
from ursamajor.models.layout import Layouts
from ursamajor.service.exceptions import contains

TIMEOUT = 10


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.content.read(), url


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        texts = await asyncio.gather(*[
            fetch(session, url)
            for url in urls
        ])
        return texts


def links_process_async(links: list):
    links_out = list()
    for raw_link in links:
        link = raw_link['link'].strip()
        if not contains(link) and not is_exist_in_db(link):
            links_out.append(link)

    outs = asyncio.run(fetch_all(links_out))
    for out in outs:
        try:
            article = fetch_main_content(out[0])
            save_page(link=out[1], html=out[0], article=article)
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
    p.is_pub = False
    try:
        p.save()
    except IntegrityError:
        pass

    p.url = p.build_url()
    p.is_pub = True
    try:
        p.save()
    except IntegrityError:
        pass


def get_section():
    return Page.publicated.filter(layout=Layouts.LAYOUT_SECTION).first()


def is_exist_in_db(link: str) -> bool:
    try:
        Page.objects.get(source_url=link)
        return True
    except Page.DoesNotExist:
        return False
