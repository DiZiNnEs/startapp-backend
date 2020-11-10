from weather_app.parser import GetWeather


class WeatherHandling:
    def __init__(self, get_weather: GetWeather) -> None:
        self.__GET_WEATHER = get_weather

    def temperature_handle(self):
        temperature = self.__GET_WEATHER.get_temperature().get('temp')
        if temperature < 0:
            return 'Одевайтесь теплее, на улице холодно'
        elif temperature <= 5:
            return 'На улице холодно, накиньте куртку'
        elif temperature <= 10:
            return 'На улице прохладно, наденьте легкую куртку'
        elif temperature <= 15:
            return 'На улице не так холодно, но расслаблять не стоит'
        elif temperature <= 20:
            return 'Погода отличная, одевайтесь более открыто'
        else:
            return 'Сервис временно не работает'

    def wind_handle(self):
        wind = self.__GET_WEATHER.get_wind()[1]
        if wind < 0:
            return 'Ветра нету'
        elif wind <= 1.5:
            return 'Тихий ветер'
        elif wind <= 3.3:
            return 'Легкий бриз'
        elif wind <= 5.4:
            return 'Слабый бриз'
        elif wind <= 7.9:
            return 'Умеренный бриз'
        elif wind <= 10.7:
            return 'Свежий бриз'
        elif wind <= 13.8:
            return 'Сильный брез'
        elif wind <= 17.8:
            return 'Крепкий ветер'
        elif wind <= 20.7:
            return 'Буря'
        elif wind <= 24.4:
            return 'Шторм (сильная буря)'
        elif wind <= 28.4:
            return 'Сильный шторм (жесткая буря)'
        elif wind <= 32.6:
            return 'Жетский шторм (жетская буря)'
        elif wind >= 32.7:
            return 'Ураган'
        else:
            return 'Сервис временно не работает'

    def humidity_handle(self):
        humidity = self.__GET_WEATHER.get_humidity()
        return f'{humidity}%'


weather = WeatherHandling(GetWeather('Kokshetau'))
weather.temperature_handle()
print(weather.wind_handle())
print(weather.humidity_handle())
