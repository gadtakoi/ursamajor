from django.db import models
from django.db.models import Q


class PublicatedPageManager(models.Manager):
    def get_queryset(self):
        queryset = super(PublicatedPageManager, self).get_queryset()
        return queryset.filter(*self.get_query())

    @classmethod
    def get_query(cls):
        return (
            Q(is_pub=True),
        )


