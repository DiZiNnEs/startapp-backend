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
