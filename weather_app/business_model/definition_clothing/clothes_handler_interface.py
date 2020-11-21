from abc import ABC, abstractmethod


class ClothesHandlerInterface(ABC):
    def __init__(self, temperature: int,
                 humidity: any,
                 wind: any,
                 headdress_dictionary: dict,
                 outerwear_dictionary: dict,
                 bottom_dictionary: dict,
                 shoes_dictionary: dict) -> None:
        self._TEMPERATURE = temperature
        self._HEADDRESS_DICTIONARY = headdress_dictionary
        self._OUTERWEAR_DICTIONARY = outerwear_dictionary
        self._BOTTOM_DICTIONARY = bottom_dictionary
        self._SHOES_DICTIONARY = shoes_dictionary

    def get_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        return self._handle_clothes_recommendation(dictionary_recommendations)

    @abstractmethod
    def _handle_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def _handle_headdress_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _handle_outerwear_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _handle_bottom_recommendation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _handle_shoes_recommendation(self) -> str:
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
