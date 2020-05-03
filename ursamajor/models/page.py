from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from tinymce_4.fields import TinyMCEModelField

from ursamajor.managers import PublicatedPageManager
from ursamajor.models import SEOMixin
from ursamajor.models.layout import Layouts


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

    layout = models.IntegerField(
        verbose_name='шаблон',
        choices=Layouts.choices,
        null=Layouts.LAYOUT_PAGE
    )

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

    def get_title(self):
        return self.seo_title or self.seo_title or self.name

    def get_h1(self):
        return self.seo_h1 or self.seo_title or self.name

    def get_content(self):
        return "<br />".join(self.content.split("\n"))

    @property
    def url_html(self) -> str:
        if self.url:
            return "/{}/".format(self.url)
        elif self.url == '' or self.url == '/':
            return "/"

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

    def __init__(self, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)
        self.articles = []

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'
