from weather_app.business_model.definition_clothing.clothes_handler_interface import ClothesHandlerInterface


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
        return self._handle_clothes_recommendation(dictionary_recommendations)

    def _handle_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        return self.__processing_everything(dictionary_recommendations)

    def handle_headdress_recommendation(self) -> str:
        return self.__processing_everything(self._HEADDRESS_DICTIONARY)

    def handle_outerwear_recommendation(self) -> str:
        return self.__processing_everything(self._OUTERWEAR_DICTIONARY)

    def handle_bottom_recommendation(self) -> str:
        return self.__processing_everything(self._BOTTOM_DICTIONARY)

    def handle_shoes_recommendation(self) -> str:
        return self.__processing_everything(self._SHOES_DICTIONARY)

    def _handle_temperature(self):
        pass

    def _handle_humidity(self):
        pass

    def _handle_wind(self):
        pass

    def __processing_everything(self, recommendation_dictionary: dict[int: str]):
        for temperature in recommendation_dictionary:
            try:
                if self._TEMPERATURE <= temperature:
                    return recommendation_dictionary[temperature]
                else:
                    continue
            except Exception as ex:
                print(ex)
