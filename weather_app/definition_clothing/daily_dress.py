from weather_app.parser import GetWeather


class DailyDress:
    def __init__(self, temperature) -> None:
        self.__TEMPERATURE = temperature

    def handle_temperature_to_dress(self) -> str:
        return self.__handle_recommendation()

    def __handle_recommendation(self) -> str:
        RECOMMENDATION = {
            -30: 'На улице мороз не выходите!',
            -25: 'На улице мороз не выходите!',
            -20: 'Одевайтесь очень тепло, шапку-ушанку и шарф обязтаельно!',
            -15: 'Одевайтесь теплее шарф с шапкой!',
            -10: 'Одевайтесь теплее если едете на большие расстояние',
            -5: 'Одевайтесь тепло!',
            0: 'Одевайтесь более менее теплее',
            5: 'Наденьте куртку и подштаники',
            10: 'Одевайтесь как бог велеет xD',
            15: 'Одевайтесь как хотите',
            20: 'На улице тепло одевайтесь свободнее',
            25: 'На улице жара!',
            30: 'Не выходите на улице жарко',
        }

        for temp in RECOMMENDATION:
            try:
                if self.__TEMPERATURE <= temp:
                    return RECOMMENDATION[temp]
                else:
                    continue
            except Exception as ex:
                print(ex)
