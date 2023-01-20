from django.urls import path

from login.views import loginfunc

urlpatterns = [
    path('', loginfunc, name='login'),
]
