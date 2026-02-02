# 🌦️ Proyecto 4: Análisis de Datos Climáticos desde una API Pública

**Nivel:** 1 — Fundamentos de Programación y Ciencia de Datos  
**Repositorio:** Ciencia_de_Datos  
**Autor:** StalkerData  

---

## 🎯 Propósito del Proyecto

El objetivo de este proyecto es **consumir datos reales desde una API REST pública**, procesarlos y analizarlos utilizando Python y herramientas básicas de ciencia de datos.

A diferencia de proyectos basados en archivos CSV locales, este ejercicio introduce una etapa clave del flujo de trabajo en ciencia de datos:

> **Adquisición de datos desde fuentes externas en tiempo real**

Este tipo de tareas es común en escenarios profesionales donde los datos provienen de servicios web, sensores, APIs abiertas o sistemas externos.

---

## 🧭 Contexto

Se desea analizar el comportamiento climático reciente de una ubicación geográfica específica (en este caso, una ciudad en Colombia), utilizando datos horarios reales obtenidos desde la API pública **Open-Meteo**.

El análisis incluye variables como:
- Temperatura
- Humedad relativa
- Precipitación
- Códigos climáticos

El objetivo **no es hacer predicción**, sino realizar exploración, análisis descriptivo y visualización básica.

---

## 🌐 Fuente de Datos

- **API:** Open-Meteo
- **Tipo:** API REST pública (sin autenticación)
- **Formato:** JSON
- **Documentación:** https://open-meteo.com/

Los datos se obtienen mediante solicitudes HTTP (`GET`) usando la librería `requests`.

---

## 🧩 Objetivos del Proyecto

### 🔹 1. Consumo de una API REST

- Realizar solicitudes HTTP con parámetros personalizados.
- Obtener datos climáticos en formato JSON.
- Comprender la estructura del response.

### 🔹 2. Transformación de datos

- Extraer la sección relevante del JSON.
- Convertir los datos horarios a un `DataFrame` de pandas.
- Verificar dimensiones, tipos de datos y consistencia.

### 🔹 3. Exploración y análisis descriptivo

- Analizar el comportamiento de las variables climáticas.
- Calcular estadísticas básicas (promedios, máximos, mínimos).
- Identificar patrones temporales simples.

### 🔹 4. Visualización de datos

- Gráficos de series temporales.
- Visualización de distribuciones.
- Interpretación visual de resultados.

### 🔹 5. Comunicación de resultados

- Extraer conclusiones claras a partir de los datos.
- Documentar hallazgos y limitaciones del análisis.

---

## 📁 Estructura del Proyecto
```
.
├── notebooks
│ └── analisis_datos.ipynb
├── results
└── requirements.txt
```

---

### 📓 notebooks/
Contiene el notebook principal donde se realiza:
- La solicitud a la API
- La transformación de los datos
- El análisis estadístico
- Las visualizaciones
- Las conclusiones

### 📊 results/
Carpeta destinada a almacenar gráficos, resultados intermedios o salidas exportadas del análisis (si aplica).

### 📦 requirements.txt
Listado de dependencias necesarias para ejecutar el proyecto.

---

## 🧠 Conceptos Reforzados

| Área | Concepto |
|----|----|
| Python | Requests, manejo de JSON |
| Pandas | DataFrames desde APIs |
| Estadística | Análisis descriptivo |
| Probabilidad | Frecuencias empíricas |
| Visualización | Gráficos básicos |
| Ciencia de Datos | Ingesta de datos externos |

---

## 🧾 Resultado Esperado

Al finalizar el proyecto se obtiene:

- Un análisis completo de datos climáticos reales.
- Visualizaciones interpretables.
- Conclusiones basadas en evidencia.
- Un flujo de trabajo reproducible desde una API externa.

---
Regresar al [README principal](../../README.md) 🏠

Regresar al [README Nivel 1](../README.md) 🏠