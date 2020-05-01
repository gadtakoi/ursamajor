from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from ursamajor.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    # path('', include('_qna.urls')),
    # path('', include('_customuser.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
