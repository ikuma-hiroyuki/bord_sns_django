from django.urls import path

from board.views import boardfunc

urlpatterns = [
    path('', boardfunc, name='board'),
]
