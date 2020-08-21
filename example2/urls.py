from django.urls import path
from . import views

app_name='sql'

urlpatterns = [
    path('', views.index, name='index'),
    path('ok/', views.index_ok, name='index_ok'),
    path('<int:pk>/', views.product_detail_view, name='details'),
]

