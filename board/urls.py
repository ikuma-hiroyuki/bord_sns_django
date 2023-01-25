from django.urls import path

from board.views import boardfunc, listfunc

urlpatterns = [
    path('', boardfunc, name='board'),
    path('list/', listfunc, name='list'),
]
