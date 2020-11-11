from django.urls import path

from .views import WeatherAPIView

urlpatterns = [
    path('kokshetau/', WeatherAPIView.as_view(), name='api for today weather')
]
