from weather_app.parser import GetWeather


class WeatherHandling:
    def __init__(self, get_weather: GetWeather) -> None:
        self.__GET_WEATHER = get_weather

    def temperature_handle(self) -> str:
        temperature = self.__GET_WEATHER.get_temperature().get('temp')
        return self.__get_temperature_interpretation(temperature)

    def wind_handle(self) -> str:
        wind_value = self.__GET_WEATHER.get_wind()[1]
        return self.__get_wind_interpretation(wind_value)

    def humidity_handle(self) -> str:
        humidity = self.__GET_WEATHER.get_humidity()
        return f'{humidity}%'

    def __get_temperature_interpretation(self, temperature: int) -> str:
        weathers = {
            0: 'Одевайтесь теплее, на улице холодно',
            5: 'На улице холодно, накиньте куртку',
            10: 'На улице прохладно, наденьте легкую куртку',
            15: 'На улице не так холодно, но расслаблять не стоит',
            20: 'Погода отличная, одевайтесь более открыто',
        }

        for weather_temperature in weathers:
            if temperature <= weather_temperature:
                return weathers[weather_temperature]
        return 'Сервис временно не работает'

    def __get_wind_interpretation(self, wind_value: int) -> str:
        wind_dict = {
            0: 'Ветра нету',
            1.5: 'Тихий ветер',
            3.3: 'Легкий бриз',
            5.4: 'Слабый бриз',
            7.9: 'Умеренный бриз',
            10.7: 'Свежий бриз',
            13.8: 'Сильный брез',
            17.8: 'Крепкий ветер',
            20.7: 'Буря',
            24.4: 'Шторм (сильная буря)',
            28.4: 'Сильный шторм (жесткая буря)',
            32.6: 'Жетский шторм (жетская буря)',
            32.7: 'Ураган',
        }

        for wind in wind_dict:
            if wind_value <= wind:
                return wind_dict[wind]
        return 'Сервис временно не работает'
