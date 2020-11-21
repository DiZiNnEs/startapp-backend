from abc import ABC, abstractmethod


class ClothesHandlerInterface(ABC):
    @abstractmethod
    def get_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def _handle_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def handle_headdress_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def handle_outerwear_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def handle_bottom_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def handle_shoes_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _handle_temperature(self):
        raise NotImplementedError

    @abstractmethod
    def _handle_humidity(self):
        raise NotImplementedError

    @abstractmethod
    def _handle_wind(self):
        raise NotImplementedError
