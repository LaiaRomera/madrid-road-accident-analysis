# Análisis de la Accidentalidad en Madrid y Predicción de Riesgo Relacionado con el Consumo de Alcohol

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar la accidentalidad vial registrada en Madrid utilizando datos abiertos proporcionados por el Ayuntamiento de Madrid.

A través de un análisis exploratorio de datos (EDA), se estudian diferentes factores relacionados con los accidentes de tráfico para identificar patrones, tendencias y posibles factores de riesgo.

Además, se desarrolló un modelo de Regresión Logística para analizar la probabilidad de obtener un resultado positivo en una prueba de alcoholemia a partir de variables demográficas y contextuales del accidente, como el tipo de día, la franja horaria, el distrito, el sexo y el rango de edad.

Las variables categóricas fueron transformadas mediante One-Hot Encoding y posteriormente escaladas utilizando StandardScaler. El conjunto de datos se dividió en entrenamiento (80%) y prueba (20%), manteniendo la proporción de casos positivos mediante estratificación.

El modelo de Regresión Logística obtuvo una precisión global (accuracy) elevada debido al fuerte desbalanceo de clases presente en el conjunto de datos. Sin embargo, no consiguió identificar correctamente los casos positivos de alcoholemia, obteniendo valores de recall y F1-score cercanos a cero.

Este resultado pone de manifiesto la importancia de seleccionar métricas adecuadas en problemas desbalanceados y plantea la necesidad de aplicar técnicas adicionales como balanceo de clases, ajuste de hiperparámetros o algoritmos alternativos.


---

## Objetivos

### Objetivo general

Analizar los accidentes de tráfico registrados en Madrid para comprender mejor los factores asociados a la accidentalidad y explorar el impacto del consumo de alcohol en este tipo de sucesos.

### Objetivos específicos

* Realizar un análisis exploratorio de los datos.
* Identificar patrones temporales y geográficos de accidentalidad.
* Estudiar la distribución de accidentes relacionados con el alcohol.
* Preparar los datos para tareas de Machine Learning.
* Entrenar un modelo de Regresión Logística.
* Evaluar la capacidad predictiva del modelo.

---

## Dataset

Los datos utilizados proceden del Portal de Datos Abiertos del Ayuntamiento de Madrid.

El conjunto de datos contiene información relacionada con accidentes de tráfico ocurridos en la ciudad, incluyendo variables como:

* Fecha y hora del accidente.
* Distrito.
* Tipo de accidente.
* Información sobre alcoholemia.
* Características asociadas al siniestro.
* Otras variables de interés para el análisis.

---

## Análisis Exploratorio de Datos (EDA)

Durante esta fase se realizaron diferentes análisis para comprender mejor la información disponible:

* Distribución temporal de los accidentes.
* Análisis por distritos.
* Identificación de patrones de accidentalidad.
* Estudio de los casos relacionados con el consumo de alcohol.
* Visualización de tendencias y comportamientos relevantes.

---

## Modelado Predictivo

Tras el proceso de limpieza y preparación de los datos, se desarrolló un modelo de Regresión Logística para explorar la capacidad predictiva de determinadas variables relacionadas con los resultados de alcoholemia.

Las principales etapas fueron:

1. Limpieza y transformación de datos.
2. Selección de variables.
3. División en conjuntos de entrenamiento y prueba.
4. Entrenamiento del modelo.
5. Evaluación de resultados.

---

## Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## Estructura del Proyecto

```
madrid-road-accident-analysis/

├── data/
├── notebooks/
├── src/
├── models/
├── README.md
└── requirements.txt
```

---

## Posibles Mejoras Futuras

* Incorporar nuevas variables explicativas.
* Comparar diferentes algoritmos de clasificación.
* Realizar un análisis más profundo de los factores de riesgo.
* Desarrollar un dashboard interactivo para la visualización de resultados.
* Actualizar el estudio con datos de años posteriores.

---

## Autor

Laia Romera

Máster en Data Science e Inteligencia Artificial.
