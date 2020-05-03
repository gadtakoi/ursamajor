from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from ursamajor.views import IndexView, PageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('articles/<str:url>/', PageView.as_view(), name='page-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
