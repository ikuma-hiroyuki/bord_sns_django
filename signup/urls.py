from django.urls import path

from signup.views import signupfunc

urlpatterns = [
    path('', signupfunc, name='signup'),
]
