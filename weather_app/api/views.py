from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from ..parser import GetWeather, WeatherHandling


class WeatherAPIView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        data = [
            {'Morning': '18°'},
            {'Evening': '20°'},
            {'Night': '11°'},
        ]
        return Response(data)


@api_view(['GET', 'POST'])
def test(request, pk):
    get_weather = GetWeather(city_name=pk)
    handle_weather = WeatherHandling(get_weather)
    data = [
        {'Temperature': handle_weather.temperature_handle()},
        {'Humidity': handle_weather.humidity_handle()},
        {'Wind': handle_weather.wind_handle()},
        {'City': pk}
    ]
    return Response(data)
