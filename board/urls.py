from django.urls import path

from board.views import signupfunc

urlpatterns = [
    path('', signupfunc),
    path('signup/', signupfunc),
]
