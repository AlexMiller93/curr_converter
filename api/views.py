from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response

from .utils import parse_latest_rates

# Create your views here.

"""
GET /api/rates?from=USD&to=RUB&value=1

{
    "result": 62.16,
}
"""

currencies = parse_latest_rates()


class HomeView(View):


    def get(self, request):

        context = {
            'currencies': currencies
        }

        return render(request, 'api/home.html', context)

    def post(self, request):
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        from_amount = int(request.POST.get('amount'))

        # result = round((currencies[from_curr] / currencies[to_curr]) * float(from_amount), 2)
        result = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'result': result
        }

        return render(request=request, template_name='api/home.html', context=context)


class ConverterView(generics.GenericAPIView):

    def get(self, request: HttpRequest):
        """

        :param request:
        :return:
        -----

        """
        currencies = parse_latest_rates()

        # try:
        from_curr = request.GET.get("from", "")
        to_curr = request.GET.get("to", "")
        value = request.GET.get("value", 0)

        try:
            value = int(value)
        except:
            return Response({"error": "Value should be a number"}, status=status.HTTP_400_BAD_REQUEST)

        # if (from_curr and to_curr) not in currencies:
        #     return Response({"error": "No valid currency"}, status=status.HTTP_400_BAD_REQUEST)

        result = round((currencies[to_curr] / currencies[from_curr]) * value, 2)

        return Response({"result": result}, status=status.HTTP_200_OK)

        # except Exception as e:
        #     return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
