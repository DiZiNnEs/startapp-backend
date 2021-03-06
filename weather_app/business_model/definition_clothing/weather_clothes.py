from weather_app.business_model.definition_clothing.weather_clothes_interface import WeatherClothesInterface
from ..common_handler import common_handler_function


class WeatherClothes(WeatherClothesInterface):
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
        return common_handler_function(dictionary_recommendations)

    def get_headdress_recommendation(self) -> str:
        return common_handler_function(self._HEADDRESS_DICTIONARY)

    def get_outerwear_recommendation(self) -> str:
        return common_handler_function(self._OUTERWEAR_DICTIONARY)

    def get_bottom_recommendation(self) -> str:
        return common_handler_function(self._BOTTOM_DICTIONARY)

    def get_shoes_recommendation(self) -> str:
        return common_handler_function(self._SHOES_DICTIONARY)
