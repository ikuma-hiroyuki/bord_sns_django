from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from board.views import boardfunc, listfunc

urlpatterns = [
    path('', boardfunc, name='board'),
    path('list/', listfunc, name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
