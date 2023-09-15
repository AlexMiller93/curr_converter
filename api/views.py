from django.http import HttpRequest
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Converter

# Create your views here.

"""
GET /api/rates?from=USD&to=RUB&value=1

{
    "result": 62.16,
}
"""


class ConverterView(generics.GenericAPIView):

    def get(self, request: HttpRequest):
        """

        :param request:
        :return:
        -----

        """
        try:
            from_curr = request.GET.get("from", "")
            to_curr = request.GET.get("to", "")
            value = int(request.GET.get("value", 0))

            converter = Converter(from_curr, to_curr, value)
            result = converter.convert_value()

            if result != "No valid data":
                data = {
                    "message": "Successfully converted!",
                    "result": result
                }

                return Response(data, status=status.HTTP_200_OK)
            else:

                message = "Something from input data wrong"

                return Response(
                    {"message": message}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
