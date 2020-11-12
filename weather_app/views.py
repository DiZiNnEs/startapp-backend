from django.http import HttpResponse
from django.views import generic

from .parser import get_weather, weather_handling


class HomeCityView(generic.TemplateView):
    template_name = 'weather_app/city_home.html'
    FileNotFoundError = HttpResponse('Error', status=500)
    NotFoundError = HttpResponse('Error', status=500)

    def get_context_data(self, **kwargs):
        get_weather_parser = get_weather.GetWeather(city_name=kwargs.get('pk'))
        weather = weather_handling.WeatherHandling(get_weather_parser)
        context = {
            'temp': weather.temperature_handle(),
            'wind': weather.wind_handle(),
            'humidity': weather.humidity_handle(),
            'pk': kwargs.get('pk'),
        }
        return context


class CityView(generic.TemplateView):
    template_name = 'weather_app/city.html'


class IndexView(generic.TemplateView):
    template_name = 'weather_app/index.html'
