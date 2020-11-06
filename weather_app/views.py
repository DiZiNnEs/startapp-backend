from django.shortcuts import render

from .parser import GetWeather


def home(request):
    weather = GetWeather('kokshetau')
    context = {
        'temperature': weather.get_temperature(),
        'humidity': weather.get_humidity(),
        'wind': weather.get_wind(),
    }
    return render(request, 'weather_app/index.html', context)
