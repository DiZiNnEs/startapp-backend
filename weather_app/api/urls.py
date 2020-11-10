from django.urls import path

from .views import test

urlpatterns = [
    path('weather/current/city=<str:pk>/', test, name='api for today weather')
]
