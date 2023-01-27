from django.contrib import admin
from django.urls import include, path

from board.views import logoutfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls'), ),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', include('board.urls')),
    path('good/<int:pk>', include('board.urls')),
    path('read/<int:pk>', include('board.urls')),
]
