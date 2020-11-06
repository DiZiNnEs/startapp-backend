from rest_framework.views import APIView
from rest_framework.response import Response


class WeatherAPIView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        data = [
            {'Morning': '18°'},
            {'Evening': '20°'},
            {'Night': '11°'},
        ]
        return Response(data)
