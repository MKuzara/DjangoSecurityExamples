from django.urls import path
from . import views

app_name='xss'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),

    # CRUD
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('post/new/', views.PostNewView.as_view(), name='new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),

    path('search/', views.search, name='search')
]
