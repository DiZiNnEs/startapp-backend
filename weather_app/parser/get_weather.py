from pyowm import OWM

from startup_project_backend.env import env


class GetWeather:
    def __init__(self, city_name: str) -> None:
        self.__API = OWM(env('OPENWEATHERAPI'))
        self.__MANAGER = self.__API.weather_manager()
        self.__WEATHER = self.__MANAGER.weather_at_place(city_name)

    def get_temperature(self) -> dict[str: int or None]:
        return self.__WEATHER.weather.temperature('celsius')

    def get_humidity(self) -> int:
        return self.__WEATHER.weather.humidity

    def get_wind(self) -> tuple[str, int]:
        return next(iter(self.__WEATHER.weather.wind().items()))
