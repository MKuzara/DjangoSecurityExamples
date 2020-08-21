from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='login'),
    path('v2/', views.login_v2, name='login_v2')
]
