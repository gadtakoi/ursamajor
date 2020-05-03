from django.db import models


class Layouts(models.IntegerChoices):
    LAYOUT_INDEX = 0, 'главная'
    LAYOUT_PAGE = 1, 'статья'
    LAYOUT_SECTION = 2, 'раздел'
