from pyowm import OWM

from startup_project_backend.env import env


class GetWeather:
    def __init__(self, city_name: str) -> None:
        self.__API = OWM(env('OPENWEATHERAPI'))
        self.__MANAGER = self.__API.weather_manager()
        self.__OBSERVATION = self.__MANAGER.weather_at_place(city_name)

    def get_weather(self) -> dict[str: int or None]:
        return self.__OBSERVATION.weather.temperature('celsius')

    def get_humidity(self) -> int:
        return self.__OBSERVATION.weather.humidity

    def get_wind(self) -> tuple[str, int]:
        return next(iter(self.__OBSERVATION.weather.wind().items()))
