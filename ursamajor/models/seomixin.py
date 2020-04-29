from django.db import models


class SEOMixin(models.Model):
    seo_h1 = models.CharField(
        '<h1>',
        max_length=255,
        default='',
        blank=True
    )
    seo_title = models.CharField(
        '<title>',
        max_length=255,
        default='',
        blank=True
    )
    seo_keywords = models.CharField(
        '<meta name="keywords">',
        max_length=255,
        default='',
        blank=True
    )
    seo_description = models.CharField(
        '<meta name="description">',
        max_length=255,
        default='',
        blank=True
    )
    seo_prevent_indexing = models.BooleanField(
        'не индексировать',
        default=False
    )

    class Meta:
        abstract = True
