from django.http import HttpResponse
from django.views import generic

from .parser import (
    get_weather,
    weather_handling,
)

from .definition_clothing import (
    DailyDress,
    Headdress,
)


class HomeCityView(generic.TemplateView):
    template_name = 'weather_app/city_home.html'

    def get_context_data(self, **kwargs):
        get_weather_parser = get_weather.GetWeather(city_name=kwargs.get('pk'))
        weather = weather_handling.WeatherHandling(get_weather_parser)
        how_dress = DailyDress(temperature=get_weather_parser.get_temperature().get('temp'))
        outerwear = Headdress(temperature=get_weather_parser.get_temperature().get('temp'))
        context = {
            'city': kwargs.get('pk'),
            'temp': f'{get_weather_parser.get_temperature().get("temp")}°',
            'wind': weather.wind_handle(),
            'humidity': weather.humidity_handle(),
            'outerwear': outerwear.get_outerwear_recommendation(),
            'what_to_wear_in_general': how_dress.handle_temperature_to_dress(),
        }

        return context


class CityView(generic.TemplateView):
    template_name = 'weather_app/city.html'


class IndexView(generic.TemplateView):
    template_name = 'weather_app/index.html'
