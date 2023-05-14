from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Temperature.models import CelsiusModel
from django.http import HttpResponse
from rest_framework.decorators import api_view
import tensorflow as tf
import numpy as np
# función auxiliar para cargar el modelo entrenado
def load_model():
    model = tf.keras.models.load_model('model.h5')
    return model
# función auxiliar para preprocesar la entrada
def preprocess_input(celsius):
    return np.array([celsius], dtype=float)
# función auxiliar para postprocesar la salida
def postprocess_output(fahrenheit):
    return str(fahrenheit[0][0])
# vista para realizar predicciones
@csrf_exempt
@api_view(['POST'])
def predict_temperature(request):
    # cargamos el modelo entrenado
    #model = load_model()
    # obtenemos la temperatura en Celsius del cuerpo de la solicitud
    # celsius = float(request.POST['celsius'])
    # preprocesamos la entrada
    #input_data = preprocess_input(celsius)
    # realizamos la predicción
    #fahrenheit = model.predict(input_data)
    # postprocesamos la salida
    #output_data = postprocess_output(fahrenheit)
    # creamos una respuesta JSON con el resultado
    response_data = {'fahrenheit': 3}
    return JsonResponse(response_data)
