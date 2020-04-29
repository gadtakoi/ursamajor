from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from config.settings import INDEX_PER_PAGE
from ursamajor.models import Page


class IndexView(View):
    def get(self, request, **kwargs):
        variant = kwargs.get('variant', '')
        page_num = request.GET.get('page', 1)
        questions_list = Page.publicated.all().order_by('-date_create')

        paginator = Paginator(questions_list, INDEX_PER_PAGE)

        try:
            questions = paginator.page(page_num)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)

        context = {
            'questions': questions,
            'variant': variant
        }

        return render(request, 'ursamajor/index.html', context)
