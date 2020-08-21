from django.contrib import admin
from django.urls import path, include

from index.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xss/', include('examples.urls', namespace='xss')),
    path('sql/', include('example2.urls', namespace='sql')),
    path('login/', include('login.urls', namespace='login')),
    path('', index, name='index'),
]
