from .weather_clothes import WeatherClothes
from weather_app.business_model.weather_handle import WeatherRecommendation


clothes_handler = WeatherClothes()
weather_recommendation = WeatherRecommendation()


def handle_recommendation():
    return clothes_handler.get_clothes_recommendation(dictionary_recommendations=weather_recommendation.underwear)


def test_handle_recommendation():
    assert handle_recommendation() == 'Наденьте куртку и подштаники'
