from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cities', views.cities, name='cities'),
    path('main', views.main, name='first try'),
    path('magic', views.magic, name='magic'),
    path('fun', views.fun, name='fun'),
    path('comments', views.comments, name='comments'),
]