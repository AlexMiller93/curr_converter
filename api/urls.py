from django.urls import path
from .views import ConverterView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('api/rates/', ConverterView.as_view(), name='converter'),
]