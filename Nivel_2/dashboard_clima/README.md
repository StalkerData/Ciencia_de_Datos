# 🌤️ Proyecto 3 — Dashboard de Visualización de Datos Climáticos con Plotly

**Nivel:** 2 — Manipulación y Análisis de Datos  
**Repositorio:** Ciencia_de_Datos  
**Autor:** StalkerData  

---

## 🎯 Propósito del Proyecto

El objetivo de este proyecto es construir un dashboard de análisis climático utilizando datos meteorológicos reales y visualizaciones interactivas.

A diferencia de los proyectos anteriores, el enfoque principal no está únicamente en procesar datos, sino también en **comunicar información de forma visual y comprensible**, aplicando principios de storytelling con datos.

Este proyecto permite consolidar conocimientos de:

- Obtención de datos desde APIs.
- Series temporales.
- Análisis exploratorio.
- Visualización interactiva con Plotly.
- Organización de información para la toma de decisiones.

---

## 📦 Fuente de Datos

Los datos fueron obtenidos mediante la API pública de:

### 🌍 Open-Meteo

https://open-meteo.com/

La API proporciona información meteorológica histórica y de pronóstico sin necesidad de autenticación.

Para este proyecto se utilizaron datos correspondientes a:

- 📍 Ciudad: Cúcuta, Colombia
- 📅 Período analizado: Mayo de 2026

---

## 🧠 Problema a Resolver

Una persona interesada en conocer el comportamiento reciente del clima de una ciudad necesita responder preguntas como:

- ¿Cómo varió la temperatura durante el período analizado?
- ¿Cuáles fueron los momentos con mayor humedad?
- ¿En qué momentos se registró precipitación?
- ¿Existen patrones visibles en los datos climáticos?

El dashboard busca responder estas preguntas de forma visual e interactiva.

---

## 🧩 Objetivos del Proyecto

### 🔹 Obtención de Datos

- Consumo de datos meteorológicos desde una API.
- Procesamiento de respuestas JSON.
- Conversión de datos a estructuras tabulares con Pandas.

### 🔹 Preparación de Datos

- Conversión de fechas y horas.
- Selección de variables relevantes.
- Organización de series temporales.

### 🔹 Análisis Exploratorio

- Comportamiento de la temperatura.
- Variación de la humedad relativa.
- Distribución de precipitaciones.
- Identificación de patrones temporales.

### 🔹 Visualización Interactiva

Construcción de gráficos interactivos utilizando Plotly:

- Temperatura vs tiempo.
- Humedad vs tiempo.
- Precipitación vs tiempo.
- Comparaciones entre variables.

### 🔹 Storytelling con Datos

Interpretación de los resultados obtenidos mediante visualizaciones y análisis descriptivo.

---

## 📊 Variables Analizadas

Entre las variables disponibles en Open-Meteo se trabajó principalmente con:

| Variable | Descripción |
|-----------|------------|
| temperature_2m | Temperatura del aire a 2 metros |
| relative_humidity_2m | Humedad relativa |
| precipitation | Precipitación |
| rain | Lluvia registrada |
| weather_code | Código meteorológico |
| time | Fecha y hora del registro |

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Uso |
|------------|-----|
| Python | Lenguaje principal |
| Pandas | Manipulación de datos |
| Plotly | Visualizaciones interactivas |
| Matplotlib | Visualizaciones complementarias |
| Jupyter Notebook | Desarrollo y análisis |
| Open-Meteo API | Fuente de datos climáticos |

---

## 🚀 Dashboard Interactivo (Implementación Adicional)

Además del notebook solicitado inicialmente, se desarrolló una versión interactiva utilizando Streamlit.

Esta implementación permite:

- Seleccionar variables climáticas.
- Explorar datos de forma dinámica.
- Visualizar gráficos interactivos desde una interfaz web.
- Aplicar filtros sin modificar código.

Aunque Streamlit no era un requisito del proyecto, se incorporó como práctica adicional para experimentar con la construcción de aplicaciones de datos.

---

## 📁 Estructura del Proyecto

```text
dashboard_clima/
├── dashboard
│   ├── app.py
│   ├── modelo
│   │   └── recolector_datos.py
│   └── vista
│       └── frontend.py
├── data
│   └── clima_cucuta_mayo_2026.csv
├── notebooks
│   └── dashboard_clima_plotly.ipynb
└── requirements.txt
```

---

## 📦 Dependencias

```
ipykernel==7.0.0
matplotlib==3.10.7
nbformat==5.10.4
numpy==2.3.3
pandas==3.0.2
plotly==6.7.0
requests-cache==1.3.1
retry-requests==2.0.0
streamlit==1.57.0
openmeteo_requests==1.7.5
```

Instalación:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar Dashboard Streamlit

Desde la carpeta del proyecto:

```bash
streamlit run dashboard/app.py
```

Esto iniciará una aplicación web local para explorar los datos climáticos de forma interactiva.

---

## 📈 Resultados Obtenidos

El proyecto permite:

- Analizar series temporales climáticas.
- Explorar patrones de temperatura y humedad.
- Identificar períodos de precipitación.
- Comparar variables meteorológicas.
- Comunicar información mediante visualizaciones interactivas.


---

## 👤 Autor

**[StalkerData](https://github.com/StalkerData)**

---

Regresar al **[Principal](../../README.md) 🏠**

Regresar al **[Nivel 2](../README.md) 🏠**