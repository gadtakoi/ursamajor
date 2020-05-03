from django.contrib import admin

from ursamajor.models import Page


@admin.register(Page)
class QuestionDataAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'parent',
                    'slug',
                    'url',
                    'is_pub'
                    )


