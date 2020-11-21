from weather_app.business_model.definition_clothing.clothes_handler_interface import ClothesHandlerInterface


class ClothesHandler(ClothesHandlerInterface):
    def _handle_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        for temperature in dictionary_recommendations:
            try:
                if self._TEMPERATURE <= temperature:
                    return dictionary_recommendations[temperature]
                else:
                    continue
            except Exception as ex:
                print(ex)

    def _handle_headdress_recommendation(self) -> str:
        for temperature in self._HEADDRESS_DICTIONARY:
            try:
                if self._TEMPERATURE <= temperature:
                    return self._HEADDRESS_DICTIONARY[temperature]
                else:
                    continue
            except Exception as ex:
                print(ex)

    def _handle_outerwear_recommendation(self) -> str:
        for temperature in self._OUTERWEAR_DICTIONARY:
            try:
                if self._TEMPERATURE <= temperature:
                    return self._OUTERWEAR_DICTIONARY[temperature]
                else:
                    continue
            except Exception as ex:
                print(ex)

    def _handle_bottom_recommendation(self) -> str:
        for temperature in self._BOTTOM_DICTIONARY:
            try:
                if self._TEMPERATURE <= temperature:
                    return self._BOTTOM_DICTIONARY[temperature]
                else:
                    continue
            except Exception as ex:
                print(ex)

    def _handle_shoes_recommendation(self) -> str:
        for temperature in self._SHOES_DICTIONARY:
            try:
                if self._TEMPERATURE <= temperature:
                    return self._SHOES_DICTIONARY[temperature]
                else:
                    continue
            except Exception as ex:
                print(ex)

    def _handle_temperature(self):
        pass

    def _handle_humidity(self):
        pass

    def _handle_wind(self):
        pass
