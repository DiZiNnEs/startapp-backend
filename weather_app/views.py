from django.views import generic

from .business_model import (
    WeatherParser,
    Weather,
    WeatherClothes,
    WeatherRecommendation,
)


class HomeCityView(generic.TemplateView):
    template_name = 'weather_app/city_home.html'

    def get_context_data(self, **kwargs):
        weather_recommendation = WeatherRecommendation()
        get_weather_parser = WeatherParser(city_name=kwargs.get('pk'))
        weather = Weather(get_weather_parser, weather_recommendation)
        clothes_handler = WeatherClothes(temperature=get_weather_parser.get_temperature().get('temp'),
                                         humidity=get_weather_parser.get_humidity(),
                                         wind=get_weather_parser.get_wind(),
                                         headdress_dictionary=weather_recommendation.headdress,
                                         outerwear_dictionary=weather_recommendation.outerwear,
                                         bottom_dictionary=weather_recommendation.underwear,
                                         shoes_dictionary=weather_recommendation.shoes, )
        context = {
            'city': kwargs.get('pk'),
            'temp': f'{get_weather_parser.get_temperature().get("temp")}°',
            'wind': weather.wind_handle(),
            'humidity': weather.humidity_handle(),
            'headdress': clothes_handler.get_headdress_recommendation(),
            'outerwear': clothes_handler.get_outerwear_recommendation(),
            'bottom': clothes_handler.get_bottom_recommendation(),
            'shoes': clothes_handler.get_shoes_recommendation(),
            'what_to_wear_in_general': clothes_handler.get_clothes_recommendation(weather_recommendation.headdress),
        }

        return context


class CityView(generic.TemplateView):
    template_name = 'weather_app/city.html'


class IndexView(generic.TemplateView):
    template_name = 'weather_app/index.html'
