from weather_app.business_model.parser import GetWeather
from .weather_recommendation import WeatherRecommendation


class WeatherHandler:
    def __init__(self, get_weather: GetWeather, weather_recommendation: WeatherRecommendation) -> None:
        self.__GET_WEATHER = get_weather
        self.__WEATHER_RECOMMENDATION = weather_recommendation

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
        weathers = self.__WEATHER_RECOMMENDATION.weathers

        for weather_temperature in weathers:
            if temperature <= weather_temperature:
                return weathers[weather_temperature]
        return 'Сервис временно не работает'

    def __get_wind_interpretation(self, wind_value: int) -> str:
        wind_dict = self.__WEATHER_RECOMMENDATION.wind

        for wind in wind_dict:
            if wind_value <= wind:
                return wind_dict[wind]
        return 'Сервис временно не работает'
