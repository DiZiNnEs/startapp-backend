from django.views import generic

from .business_model import (
    GetWeather,
    WeatherHandling,
    ClothesHandler,
)


class HomeCityView(generic.TemplateView):
    template_name = 'weather_app/city_home.html'
    __RECOMMENDATION = {
        -75: 'Старайтесь одеть голову максимально тепло #10',
        -70: 'Старайтесь одеть голову максимально тепло #9',
        -65: 'Старайтесь одеть голову максимально тепло #8',
        -60: 'Старайтесь одеть голову максимально тепло #7',
        -55: 'Старайтесь одеть голову максимально тепло #6',
        -50: 'Старайтесь одеть голову максимально тепло #5',
        -45: 'Старайтесь одеть голову максимально тепло #4',
        -40: 'Старайтесь одеть голову максимально тепло #3',
        -35: 'Старайтесь одеть голову максимально тепло #2',
        -30: 'На улице мороз не выходите!',
        -25: 'На улице мороз не выходите!',
        -20: 'Одевайтесь очень тепло, шапку-ушанку и шарф обязтаельно!',
        -15: 'Одевайтесь теплее шарф с шапкой!',
        -10: 'Одевайтесь теплее если едете на большие расстояние',
        -5: 'Одевайтесь тепло!',
        0: 'Одевайтесь более менее теплее',
        5: 'Наденьте куртку и подштаники',
        10: 'Одевайтесь как бог велеет xD',
        15: 'Одевайтесь как хотите',
        20: 'На улице тепло одевайтесь свободнее',
        25: 'На улице жара!',
        30: 'Не выходите на улице жарко',
        35: 'Ничего на голову не нужно #3',
        40: 'Ничего на голову не нужно #4',
        45: 'Ничего на голову не нужно #5',
        50: 'Ничего на голову не нужно #6',
        55: 'Ничего на голову не нужно #7',
        60: 'Ничего на голову не нужно #8',
        65: 'Ничего на голову не нужно #9',
    }

    def get_context_data(self, **kwargs):
        get_weather_parser = GetWeather(city_name=kwargs.get('pk'))
        weather = WeatherHandling(get_weather_parser)
        clothes_handler = ClothesHandler(temperature=get_weather_parser.get_temperature().get('temp'))
        context = {
            'city': kwargs.get('pk'),
            'temp': f'{get_weather_parser.get_temperature().get("temp")}°',
            'wind': weather.wind_handle(),
            'humidity': weather.humidity_handle(),
            'headdress': clothes_handler.get_recommendation(self.__RECOMMENDATION),
            'outerwear': clothes_handler.get_recommendation(self.__RECOMMENDATION),
            'bottom': clothes_handler.get_recommendation(self.__RECOMMENDATION),
            'shoes': clothes_handler.get_recommendation(self.__RECOMMENDATION),
            'what_to_wear_in_general': clothes_handler.get_recommendation(self.__RECOMMENDATION),
        }

        return context


class CityView(generic.TemplateView):
    template_name = 'weather_app/city.html'


class IndexView(generic.TemplateView):
    template_name = 'weather_app/index.html'
