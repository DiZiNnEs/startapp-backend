from pyowm import OWM

from startup_project_backend.env import env
from pyowm.commons import exceptions

from pyowm.weatherapi25.observation import Observation


class GetWeather:
    def __init__(self, city_name: str) -> None:
        self.__CITY_NAME = city_name
        self.__API = OWM(env('OPENWEATHERAPI'))
        self.__MANAGER = self.__API.weather_manager()

    def get_temperature(self) -> dict[str: int or None]:
        return self.__get_weather().weather.temperature('celsius')

    def get_humidity(self) -> int:
        return self.__get_weather().weather.humidity

    def get_wind(self) -> tuple[str, int]:
        return next(iter(self.__get_weather().weather.wind().items()))

    def __get_weather(self) -> Observation:
        try:
            weather_result = self.__MANAGER.weather_at_place(self.__CITY_NAME)
        except exceptions.NotFoundError:
            weather_result = self.__MANAGER.weather_at_place('Astana')
        return weather_result