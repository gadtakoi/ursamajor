import json
import requests

from config.settings import YNDX_TRNS_URL
from ursamajor.models import Page

TIMEOUT = 10


def run():
    pages = Page.objects.filter(translated=False)
    for page in pages:
        raw_content = page.raw_content.strip()
        raw_name = page.name.strip()
        if raw_content:
            data = {
                'text': raw_name
            }
            result_name = requests.post(url=YNDX_TRNS_URL, data=data, timeout=TIMEOUT)
            name = json.loads(result_name.content)
            data = {
                'text': raw_content[:10000]
            }
            result_content = requests.post(url=YNDX_TRNS_URL, data=data, timeout=TIMEOUT)
            text = json.loads(result_content.content)
            if text['code'] == 200:
                page.seo_title = name['text'][0]
                page.content = text['text'][0]
                page.translated = True
                page.save()
            else:
                print('text code==', text['code'])
