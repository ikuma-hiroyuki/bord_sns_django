from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from board.views import boardfunc, detailfunc, goodfunc, listfunc, readfunc

urlpatterns = [
    path('', boardfunc, name='board'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('list/', listfunc, name='list'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
