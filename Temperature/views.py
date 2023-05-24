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
# @api_view(['POST'])
# def predict_temperature(request):
#     model = load_model()
#     celsius = request.data.get('celsius')
    

#   # Utiliza request.POST.get() en lugar de request.POST[]
    
#     if celsius is not None:
#         celsius = float(celsius)
#         input_data = preprocess_input(celsius)
#         fahrenheit = model.predict(input_data)
#         output_data = postprocess_output(fahrenheit)
#         response_data = {'fahrenheit': output_data}  # Utiliza la salida procesada en lugar de un valor fijo
#         return JsonResponse(response_data)
#     else:
#         error_data = {'error': 'No se proporcionó la temperatura en Celsius'}
#         return JsonResponse(error_data, status=400)
@api_view(['POST', 'GET'])
def predict_temperature(request):
    if request.method == 'POST':
        model = load_model()
        celsius = request.data.get('celsius')
        if celsius is not None:
            celsius = float(celsius)
            input_data = preprocess_input(celsius)
            fahrenheit = model.predict(input_data)
            output_data = postprocess_output(fahrenheit)
            response_data = {'fahrenheit': output_data}
            return JsonResponse(response_data)
        else:
            error_data = {'error': 'No se proporcionó la temperatura en Celsius'}
            return JsonResponse(error_data, status=400)
    elif request.method == 'GET':
        # Lógica para manejar solicitudes GET
        # Puedes devolver una respuesta vacía o algún otro tipo de información según sea necesario
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)