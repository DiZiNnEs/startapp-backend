from django.views import generic

from .business_model import (
    GetWeather,
    WeatherHandler,
    ClothesHandler,
    WeatherRecommendation,
)


class HomeCityView(generic.TemplateView):
    template_name = 'weather_app/city_home.html'

    def get_context_data(self, **kwargs):
        get_weather_parser = GetWeather(city_name=kwargs.get('pk'))
        weather = WeatherHandler(get_weather_parser)
        clothes_handler = ClothesHandler(temperature=get_weather_parser.get_temperature().get('temp'))
        weather_recommendation = WeatherRecommendation()
        context = {
            'city': kwargs.get('pk'),
            'temp': f'{get_weather_parser.get_temperature().get("temp")}°',
            'wind': weather.wind_handle(),
            'humidity': weather.humidity_handle(),
            'headdress': clothes_handler.get_recommendation(weather_recommendation.headdress),
            'outerwear': clothes_handler.get_recommendation(weather_recommendation.headdress),
            'bottom': clothes_handler.get_recommendation(weather_recommendation.headdress),
            'shoes': clothes_handler.get_recommendation(weather_recommendation.headdress),
            'what_to_wear_in_general': clothes_handler.get_recommendation(weather_recommendation.headdress),
        }

        return context


class CityView(generic.TemplateView):
    template_name = 'weather_app/city.html'


class IndexView(generic.TemplateView):
    template_name = 'weather_app/index.html'
