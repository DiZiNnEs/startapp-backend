from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),
    path('city/', views.city, name='city'),
    path('home/city=<str:pk>', views.home_city, name='home_city')
]