from django.urls import path
from .views import predict_temperature


urlpatterns = [
    path('',predict_temperature, name='urlTemperature'),
]