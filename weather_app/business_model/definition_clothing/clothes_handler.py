from weather_app.business_model.definition_clothing.clothes_handler_interface import ClothesHandlerInterface
from ..common_handler import temperature_handler


class ClothesHandler(ClothesHandlerInterface):
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
        return temperature_handler(dictionary_recommendations)

    def _handle_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        return temperature_handler(dictionary_recommendations)

    def handle_headdress_recommendation(self) -> str:
        return temperature_handler(self._HEADDRESS_DICTIONARY)

    def handle_outerwear_recommendation(self) -> str:
        return temperature_handler(self._OUTERWEAR_DICTIONARY)

    def handle_bottom_recommendation(self) -> str:
        return temperature_handler(self._BOTTOM_DICTIONARY)

    def handle_shoes_recommendation(self) -> str:
        return temperature_handler(self._SHOES_DICTIONARY)

    def _handle_temperature(self):
        pass

    def _handle_humidity(self):
        pass

    def _handle_wind(self):
        pass
