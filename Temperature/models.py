import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

class CelsiusModel:
    def __init__(self): 
    #declaración de arreglo de ejemplo para el entrenamiento de la red neuronal#
        self._celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
        self._fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
        self._model = None

    #el optimizador permite a la red saber como ajustar los pesos y sesgos eficientemente, que cada vez aprenda más en lugar de lo contrario#
    def train_model(self):
        oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
        oculta2 = tf.keras.layers.Dense(units=3)
        salida = tf.keras.layers.Dense(units=1)
        self._model = tf.keras.Sequential([oculta1, oculta2, salida])
        #el valor numerico es la tasa de aprendizaje, en caso de ser muy pequeño aprendera muy lento, pero si es muy grande puede que supere el valor esperado#
        self._model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')
        print("Comenzando entrenamiento...")
        #Se indican los datos entrada y resultados esperados, además de la cantidad de vueltas de verificación hará, si el número es grande se podrá optimizar mejor#
        historial = self._model.fit(self._celsius, self._fahrenheit, epochs=600, verbose=False)
        print("Modelo entrenado!")
        #funcion de perdida que indica que tan mal estan los resultados en cada vuelta que dio#
        plt.xlabel("# Epoca")
        plt.ylabel("Magnitud de pérdida")
        plt.plot(historial.history["loss"])
        plt.show()

        # Guardar el modelo entrenado en un archivo 'model.h5'
        self._model.save("model.h5")
        print("Modelo guardado en 'model.h5'")

    def predict_fahrenheit(self, celsius):
        return self._model.predict([celsius])

#impresión del resultado en Fahrenheit según los Celsius ingresados por el usuario#
class CelsiusView:
    def get_celsius(self):
        return float(input("Ingrese temperatura en Celsius: "))

    def show_fahrenheit(self, ahrenheit):
        print("El resultado es " + str(fahrenheit) + " Fahrenheit!")

#Se juntan la comunicacion entre modelo y vista#
class CelsiusController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def convert(self):
        self._model.train_model()
        celsius = self._view.get_celsius()
        fahrenheit = self._model.predict_fahrenheit(celsius)
        self._view.show_fahrenheit(fahrenheit)

#cada parte son instancias donde se llama cada parte de la red neuronal para conectarlo como MVC#
if __name__ == '__main__':
    model = CelsiusModel()
    view = CelsiusView()
    controller = CelsiusController(model, view)
    controller.convert() # Llama el metodo convert del controlador, este maneja el flujo de la aplicacion solicitando la entrada del usuario, hacer las prediccion desde el modelo y mostrar el resultado en la vista

