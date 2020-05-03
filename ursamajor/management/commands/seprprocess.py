from django.core.management.base import BaseCommand

from ursamajor.service.fetcher_async import links_process_async
from ursamajor.service.serp import seprprocess
from ursamajor.service.fetcher import links_process
from ursamajor.service.translate import run as translate_run


class Command(BaseCommand):
    def handle(self, *args, **options):
        links = seprprocess()
        # links_process(links)
        links_process_async(links)
        translate_run()
