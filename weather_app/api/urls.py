from django.urls import path

from .views import WeatherAPIView

urlpatterns = [
    path('today/', WeatherAPIView.as_view(), name='api for today weather')
]
