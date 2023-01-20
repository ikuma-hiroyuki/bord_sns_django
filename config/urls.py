from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls')),
]
