from abc import ABC, abstractmethod


class WeatherClothesInterface(ABC):
    @abstractmethod
    def get_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_headdress_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_outerwear_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_bottom_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_shoes_recommendation(self) -> str:
        raise NotImplementedError
