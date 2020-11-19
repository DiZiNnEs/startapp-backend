from weather_app.business_model.definition_clothing.clothes_handler_interface import ClothesHandlerInterface


class ClothesHandler(ClothesHandlerInterface):
    def _handle_recommendation(self, recommendation: dict) -> str:
        for temp in recommendation:
            try:
                if self._TEMPERATURE <= temp:
                    return recommendation[temp]
                else:
                    continue
            except Exception as ex:
                print(ex)
