from pyowm import OWM

from pyowm.commons import exceptions
from pyowm.weatherapi25.observation import Observation

from startup_project_backend.env import env
from .weather_parser_interface import WeatherParserInterface


class WeatherParser(WeatherParserInterface):
    def __init__(self, city_name: str) -> None:
        self.__CITY_NAME = city_name
        self.__API = OWM(env('OPENWEATHERAPI'))
        self.__WEATHER_MANAGER = self.__API.weather_manager()

    def get_temperature(self) -> dict[str: int or None]:
        return self._get_weather_information().weather.temperature('celsius')

    def get_humidity(self) -> int:
        return self._get_weather_information().weather.humidity

    def get_wind(self) -> tuple[str, int]:
        return next(iter(self._get_weather_information().weather.wind().items()))

    def _get_weather_information(self) -> Observation:
        try:
            weather_result = self.__WEATHER_MANAGER.weather_at_place(self.__CITY_NAME)
        except exceptions.NotFoundError:
            weather_result = self.__WEATHER_MANAGER.weather_at_place('Astana')
        return weather_result
