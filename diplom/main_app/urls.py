from django.urls import path
from . import views

urlpatterns = [
    path('main', views.news, name='main'),
    path('register', views.register, name='register'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
]