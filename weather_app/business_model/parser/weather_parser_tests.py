from .weather_parser import WeatherParser

get_weather = WeatherParser(city_name='London')


def test_get_temperature():
    assert type(get_weather.get_temperature()) == dict


def test_get_humidity():
    assert type(get_weather.get_humidity()) == int


def test_get_wind():
    assert type(get_weather.get_wind()) == tuple
