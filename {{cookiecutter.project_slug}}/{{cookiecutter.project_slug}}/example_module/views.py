from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ExampleView(APIView):
    """
    Hello World
    """

    def get(self, request, *args, **kwargs):

        return Response(
            {
                "content": "Hello World!"
            }
        )
