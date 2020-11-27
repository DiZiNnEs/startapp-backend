from weather_app.business_model.parser import WeatherParser
from .weather_recommendation import WeatherRecommendation
from ..common_handler import common_handler_function


class Weather:
    def __init__(self, get_weather: WeatherParser, weather_recommendation: WeatherRecommendation) -> None:
        self.__GET_WEATHER = get_weather
        self.__WEATHER_RECOMMENDATION = weather_recommendation

    def temperature_handle(self) -> str:
        return self.__get_temperature_interpretation()

    def wind_handle(self) -> str:
        return self.__get_wind_interpretation()

    def humidity_handle(self) -> str:
        humidity = self.__GET_WEATHER.get_humidity()
        return f'{humidity}%'

    def __get_temperature_interpretation(self) -> str:
        weathers = self.__WEATHER_RECOMMENDATION.weathers
        return common_handler_function(weathers, 2)

    def __get_wind_interpretation(self) -> str:
        wind_dict = self.__WEATHER_RECOMMENDATION.wind
        return common_handler_function(wind_dict, 2)
