import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius = np.array([-40,-10,0,8,15,22,38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Diseñar red neuronal
"""
units registra la cantidad de neuronas de la capa, 
y con input_shape indicamos la cantidad de neuronas de ENTRADA registrando la capa de entrada. 
"""
capa = tf.keras.layers.Dense(units=1, input_shape=[1])


"""
Ejemplo de trabajar con capas intermedias.
Nos daremos cuenta con matplotlib que el aprendizaje es mucho más rápido:
"""
# capa1 = tf.keras.layers.Dense(units=3, input_shape=[1])
# capa2 = tf.keras.layers.Dense(units=3)
# salida = tf.keras.layers.Dense(units=1)

# modelo = tf.keras.Sequential([capa1, capa2, salida])

"""
Modelo de keras para darle las capas y poder trabajar con él.
Hay varios tipos de modelos, usaremos el Sequential:
"""
modelo = tf.keras.Sequential([capa])
# ya tenemos el modelo listo
# el siguiente paso es compilarlo, prepara el modelo para ser 
# entrenado. El entrenamiento es la parte mágica del machine learning:
modelo.compile(
    # propiedades de cómo queremos que procese:
    # optimizador: usaremos ADAM que permita mejorar, cuyo parámetro es
    # un número que le permite ajustar los pesos y sesgos. 
    optimizer=tf.keras.optimizers.Adam(0.1),
    # para la función de pérdida usaremos MEAN_SQUARES_ERROR
    # que configura una poca cantidad de errores grandes, que es mejor que una gran cantidad
    # de errores pequeños:
    loss='mean_squared_error'
)
# ahora sí, entrenamos el modelo:
print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado!")

if __name__ == "__main__":
    print("Hagamos una predicción!")
    # resultado = modelo.predict([100.0])
    resultado = modelo.predict(np.array([28.0]))
    print("El resultado es " + str(resultado) + " fahrenheit!")

    # Gráfica de la evolución del error (pérdida)
    """
    ¿Qué verás?
    Una gráfica con el error disminuyendo a medida que avanzan las épocas. 
    Esto te muestra que el modelo está aprendiendo y ajustando sus pesos correctamente.
    """
    plt.plot(historial.history['loss'])
    plt.title('Evolución del error durante el entrenamiento')
    plt.xlabel('Época')
    plt.ylabel('Pérdida (MSE)')
    plt.grid(True)
    plt.show()

    # Ver la estructura interna de la red neuronal, qué datos se asignaron después del entrenamiento
    # a la conección y el sesgo:
    print("Variables internas del modelo después del entrenamiento:")
    print(capa.get_weights())
    # print(capa1.get_weights())
    # print(capa2.get_weights())
    # print(salida.get_weights())