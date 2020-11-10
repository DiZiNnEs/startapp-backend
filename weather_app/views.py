from django.shortcuts import render

from .parser import GetWeather


def home(request):
    city_name = str(request.POST.get('city_name'))

    weather = GetWeather(str(city_name))
    context = {
        'temperature': weather.get_temperature(),
        'humidity': weather.get_humidity(),
        'wind': weather.get_wind(),
    }

    return render(request, 'weather_app/index.html', context)
