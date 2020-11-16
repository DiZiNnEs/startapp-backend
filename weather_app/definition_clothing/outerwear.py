from weather_app.parser import GetWeather


class Outerwear:
    def __init__(self, temperature) -> None:
        self.__TEMPERATURE = temperature

    def __handle_outerwear(self):
        RECOMMENDATION = {
            -30: 'Старайтесь одеть голову максимально тепло',
            -25: 'Шапку ушанка!',
            -20: 'Теплую шапку или шапку ушанаку',
            -15: 'Теплую шапку или шапку ушанаку #2!',
            -10: 'Теплую шапку или шапку ушанаку #3',
            -5: 'Одевайте шапку',
            0: 'Тепленкую шапочку',
            5: 'Шапочку',
            10: 'Теплую кепчку с ушами',
            15: 'Кепку',
            20: 'Капюшон',
            25: 'Ничего на голову не нужно',
            30: 'Ничего на голову не нужно',
        }
        try:
            for outerwear in RECOMMENDATION:
                if self.__TEMPERATURE <= outerwear:
                    return RECOMMENDATION.get(outerwear)
                else:
                    continue
        except Exception as ex:
            print(ex)

    def get_outerwear_recommendation(self):
        return self.__handle_outerwear()
