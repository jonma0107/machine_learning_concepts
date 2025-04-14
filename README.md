# 🤖 ¿Cómo sabe la red neuronal que debe convertir de Celsius a Fahrenheit?

## ¡Excelente pregunta! 🧠🔥

La red neuronal no sabe de antemano que debe convertir de Celsius a Fahrenheit. Nadie le dice “haz esta fórmula” ni se le programa directamente la conversión.

Lo que hace es **aprender por ejemplo**. Vamos a explicarlo más claramente:

---

## 🔁 ¿Cómo aprende la red?

Tú le das pares de datos:

```python
celsius     = [-40, -10,   0,  8, 15, 22, 38]
fahrenheit  = [-40,  14,  32, 46, 59, 72,100]
```

La red ve que:

- Cuando el input es 0, la salida debe ser 32.
- Cuando es 100, debería ser 212 (aunque no se lo diste, puede aprender a estimarlo).

Así con todos los pares.

Entonces **ajusta sus pesos internos** para minimizar el error entre lo que predice y lo que debería predecir.

---

## 📐 ¿Qué es lo que realmente aprende?

La red aprende una función matemática parecida a:

```python
salida = input × W + B
```

donde:

- `W` es el **peso**
- `B` es el **sesgo** (bias)

La red empieza con valores aleatorios de `W` y `B`, y al ver los datos muchas veces (épocas), los ajusta para que la salida se parezca lo más posible a la real (Fahrenheit).

---

## 🔬 Ejemplo más claro:

Supón que empieza con:

```python
W = 1.0
B = 0.0
```

Entonces:

Con input 0:
```python
salida = 0 × 1.0 + 0 = 0
```

Pero debería ser 32 → está muy mal → ¡ajusta!

Después de muchas iteraciones (épocas), puede terminar con:

```python
W ≈ 1.8
B ≈ 32.0
```

¡Que es justo la fórmula de conversión de Celsius a Fahrenheit! 😄

---

## 🧪 Conclusión

La red no sabe la fórmula, **aprende el patrón** a partir de los ejemplos que tú le das.

---

# 🧠 ¿De dónde saca la IA el peso (W) y el sesgo (B)?

La **IA no sabe de antemano** que el peso debe ser `1.8` y el sesgo debe ser `32`. Eso lo **aprende a través del entrenamiento** usando los datos que tú le das. Aquí te explico paso a paso:

## 🔁 El proceso de entrenamiento

1. **Inicialización aleatoria**:
   Al inicio, la red neuronal asigna valores aleatorios para los pesos (`W`) y el sesgo (`B`). Por ejemplo:
   ```python
   W = 0.5
   B = 0.1
   ```

2. **Hace predicciones con esos valores**:
   Usa la fórmula:
   ```
   salida_predicha = entrada * W + B
   ```
   Si le das `0°C`, por ejemplo, con esos valores saldría `0.5 * 0 + 0.1 = 0.1°F`, lo cual está muy lejos de los `32°F` que debería ser.

3. **Calcula el error**:
   Se compara la salida predicha con la salida real (etiquetada), y se calcula cuánto se equivocó.

4. **Ajusta los valores**:
   Usando un algoritmo llamado **backpropagation** junto con un **optimizador** (como Adam), ajusta un poco los valores de `W` y `B` para que el error sea menor en la siguiente predicción.

5. **Repite muchas veces**:
   Esto se hace miles de veces (las llamadas **épocas**) hasta que encuentra valores de `W` y `B` que minimicen el error.

---

## 📐 ¿Cómo termina con W ≈ 1.8 y B ≈ 32?

Porque esos son los valores que, al aplicar a la fórmula `entrada × W + B`, dan resultados muy cercanos a los Fahrenheit reales.

Por ejemplo:

```python
W = 1.8
B = 32

entrada = 0
salida = 0 × 1.8 + 32 = 32
entrada = 100
salida = 100 × 1.8 + 32 = 212
```

Entonces, sin saber la fórmula exacta, el modelo **la descubre** a partir de los ejemplos que le diste (¡ese es el poder del aprendizaje automático!).

---

## 🧪 Conclusión final

> La IA no tiene la fórmula de Celsius a Fahrenheit. **Aprende los parámetros (W y B)** observando los ejemplos, probando combinaciones, cometiendo errores y ajustando hasta que se acerque lo más posible a los resultados correctos.

