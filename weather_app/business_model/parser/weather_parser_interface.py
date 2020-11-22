from abc import ABC, abstractmethod

from pyowm.weatherapi25.observation import Observation


class WeatherParserInterface(ABC):

    @abstractmethod
    def get_temperature(self) -> dict[str: int or None]:
        raise NotImplementedError

    @abstractmethod
    def get_humidity(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_wind(self) -> tuple[str, int]:
        raise NotImplementedError

    @abstractmethod
    def _get_weather_information(self) -> Observation:
        raise NotImplementedError
