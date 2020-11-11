from django.shortcuts import render

from .parser import GetWeather


def home(request):
    # city_name = str(request.POST.get('city_name'))
    # while city_name is 'None':
    #     print('City name:', city_name)
    #     if city_name is not 'None':
    #         break
    #
    # weather = GetWeather(str(city_name))
    # context = {
    #     'temperature': weather.get_temperature(),
    #     'humidity': weather.get_humidity(),
    #     'wind': weather.get_wind(),
    # }

    return render(request, 'weather_app/home.html', {})


def index(request):
    return render(request, 'weather_app/index.html', {})


def city(request):
    return render(request, 'weather_app/city.html', {})


def home_city(request, pk):
    print(pk)
    context = {
        'temp': '920',
        'wind': 'Ветер сильныйй',
        'humidity': '90% влажность',
        'pk': pk,
    }

    return render(request, 'weather_app/city_home.html', context)
