from .get_weather import GetWeather

get_weather = GetWeather(city_name='London')


def test_temperature():
    assert type(get_weather.get_temperature()) == dict


def test_humidity():
    assert type(get_weather.get_humidity()) == int


def test_wind():
    assert type(get_weather.get_wind()) == tuple
