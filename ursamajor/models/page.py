from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import Truncator
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from tinymce_4.fields import TinyMCEModelField

from config.settings import MEDIA_URL
from ursamajor.managers import PublicatedPageManager
from ursamajor.models import SEOMixin


class Page(MPTTModel, SEOMixin):
    objects = models.Manager()
    publicated = PublicatedPageManager()

    name = models.CharField(verbose_name='название', max_length=255)
    slug = models.CharField(verbose_name='псевдоним', max_length=50, default='', blank=True)
    url = models.CharField(verbose_name='URL', max_length=255, blank=True, unique=True)
    image = models.ImageField(verbose_name='изображение', null=True, blank=True)

    is_pub = models.BooleanField(verbose_name='опубликовано', default=True)
    date_create = models.DateTimeField(verbose_name='время создания', auto_now_add=True, null=True)
    update_time = models.DateTimeField(verbose_name='время обновления', auto_now=True, editable=True)
    content = TinyMCEModelField(verbose_name='содержимое', blank=True)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='раздел',
        on_delete=models.CASCADE
    )

    LAYOUT_INDEX = 0
    LAYOUT_PAGE = 1

    layouts = {
        'index': (LAYOUT_INDEX, 'главная'),
        'article': (LAYOUT_PAGE, 'статья'),
    }

    choose_layout = (
        (LAYOUT_INDEX, 'главная'),
        (LAYOUT_PAGE, 'статья'),
    )

    layout = models.IntegerField(
        verbose_name='шаблон',
        choices=choose_layout,
        null=True
    )

    preview = models.TextField(null=True, verbose_name="Текст превью", blank=True, default='')

    source_url = models.CharField(null=True, blank=True, default='', max_length=255)
    raw_html = models.TextField(null=True, blank=True, default='')
    raw_content = models.TextField(null=True, blank=True, default='')
    translated = models.BooleanField(default=False)

    def get_absolute_url(self):
        if self.is_index():
            return reverse('index')
        else:
            return reverse('page', args=(self.url,))

    def is_index(self):
        return self.url == ''

    def build_url(self):
        chunks = []
        nonempty = lambda slug: bool(slug.strip())
        ancestors = lambda root, include_self=False: (
            root.get_ancestors(include_self=include_self)
        )
        if self.pk:
            chunks.extend((p.slug for p in ancestors(self) if p.slug != '/'))
        elif self.parent:
            chunks.extend((p.slug for p in ancestors(self.parent, True) if
                           p.slug != '/'))
        chunks.append(self.slug)
        if self.slug == '/':
            return ''
        url = '/'.join(filter(nonempty, chunks))
        return url

    def get_title(self):
        return self.seo_title or self.name

    def get_h1(self):
        return self.seo_h1 or self.name

    def get_articles(self, req=None):
        queryset = self.get_descendants().filter(*Page.articles.get_query())
        return queryset.order_by('-position', '-pub_time')

    def get_pub_siblings(self, include_self=False):

        if self.is_root_node():
            queryset = self._tree_manager._mptt_filter(parent=None)
        else:
            parent_id = getattr(self, self._mptt_meta.parent_attr + '_id')
            queryset = self._tree_manager._mptt_filter(parent__pk=parent_id,
                                                       is_pub=True)
        if not include_self:
            queryset = queryset.exclude(pk=self.pk)
        return queryset

    def get_subsection_items(self):
        query = Page.publicated.get_query() + (Q(layout=Page.LAYOUT_ARTICLE) | Q(layout=Page.LAYOUT_CALC),)
        return self.get_descendants().filter(*query).order_by('-position', '-pub_time')

    def get_content_preview(self):
        text = strip_tags(self.content)
        return Truncator(text).chars(self.MAX_CONTENT_PREVIEW_LEN)

    @property
    def url_html(self) -> str:
        if self.url:
            return '/' + self.url + '/'
        elif self.url == '' or self.url == '/':
            return '/'

    def __init__(self, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)
        self.articles = []

    @property
    def domain(self):
        return self.site_settings.site.domain

    @property
    def schema(self):
        if self.site_settings.use_https:
            return 'https'
        else:
            return 'http'

    def get_host(self):
        return "{}://{}".format(self.schema, self.domain)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'
