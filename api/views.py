from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import parse_latest_rates

# Create your views here.

"""
Request example 
GET /api/rates?from=USD&to=RUB&value=1

{
    "result": 62.16,
}
"""

# get dict with data about currencies code and rate some currency to euro
currencies = parse_latest_rates()


class HomeView(View):
    """ View for Currency converter API via visual app with html templates. """

    def get(self, request):
        """ Returns a dictionary with currencies info - code and rate. """

        context = {
            'currencies': currencies
        }

        return render(request, 'api/home.html', context)

    def post(self, request):
        """ Returns a response with amount converted from one to the another currency. """

        # Getting parameters of the request
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        try:
            from_amount = float(request.POST.get('amount'))
        except:
            context = {"error": "Value is empty, enter a value"}
            return render(request, template_name='api/home.html', context=context)

        result = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

        context = {
            'from_amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'result': result
        }

        return render(request=request, template_name='api/home.html', context=context)


class ConverterView(APIView):
    """ View for Currency converter API via GET method"""

    from_param = openapi.Parameter(
        name="from",
        in_=openapi.IN_QUERY,
        description="First currency",
        type=openapi.TYPE_STRING,
        required=True
    )

    to_param = openapi.Parameter(
        name="to",
        in_=openapi.IN_QUERY,
        description="Second currency",
        type=openapi.TYPE_STRING,
        required=True
    )

    value_param = openapi.Parameter(
        name="value",
        in_=openapi.IN_QUERY,
        description="Value to convert",
        type=openapi.TYPE_NUMBER,
        required=True
    )

    default_response = openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "message": openapi.Schema(type=openapi.TYPE_STRING),
                "result": openapi.Schema(type=openapi.TYPE_NUMBER)
            }
        ),
        examples={
            "application/json": {
                "message": "success",
                "result": 5.12
            }
        }
    )

    @swagger_auto_schema(
        operation_description="Converts an amount of a currency into another currency.",
        operation_id="ConvertsAnAmount",
        manual_parameters=[from_param, to_param, value_param],
        responses={200: default_response},
        tags=["Convert an amount"]
    )
    def get(self, request: HttpRequest):
        """Returns a response with amount converted for the second currency.

        :param request: The Django Request Object.
        -----
        :returns response: Response with the message of success or failed,
            the amount converted in case of success and the request's status code.

        """

        # get dict with data about currencies code and rate some currency to euro
        currencies = parse_latest_rates()

        # Getting parameters of the request
        from_curr = request.GET.get("from", "")
        to_curr = request.GET.get("to", "")
        value = request.GET.get("value", 0)

        # check some conditions and return suitable response
        if from_curr == to_curr:
            return Response({"message": "fail", "warning": f"You want to convert the same currency - {from_curr}"},
                            status=status.HTTP_400_BAD_REQUEST)

        if from_curr not in currencies or to_curr not in currencies:
            return Response({"message": "fail", "error": "No valid currency"},
                            status=status.HTTP_400_BAD_REQUEST)

        # calculate the result
        result = round((currencies[to_curr] / currencies[from_curr]) * float(value), 2)

        return Response({"message": "success", "result": result}, status=status.HTTP_200_OK)
