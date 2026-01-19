# 🪙 Analizador de Precios Históricos de Criptomonedas

## 📌 Descripción del Proyecto

Este proyecto consiste en el análisis exploratorio de los precios históricos de una criptomoneda (Bitcoin), utilizando un conjunto de datos real en formato CSV.

El objetivo **no es predecir precios**, sino practicar los fundamentos de la ciencia de datos: carga de datos, limpieza, análisis descriptivo y visualización básica.

Este proyecto forma parte del **Nivel 1 – Fundamentos de Programación para Ciencia de Datos**.

---

## 🎯 Propósito General

Desarrollar un análisis claro y estructurado que permita entender:

- El comportamiento histórico del precio de Bitcoin.
- La variabilidad y dispersión de los precios.
- La relación entre precio y volumen.
- El uso de herramientas básicas de análisis de datos en Python.

---

## 🧭 Contexto del Problema

Imagina que trabajas para una pequeña startup interesada en comprender cómo se ha comportado el precio de Bitcoin a lo largo del tiempo.

Se te entrega un archivo CSV con información histórica (fecha, precios y volumen), y tu tarea es:

- Procesar los datos.
- Analizarlos de forma descriptiva.
- Presentar conclusiones claras basadas en gráficos y estadísticas simples.

---

## 📂 Dataset Utilizado

- **Nombre:** BTC - USD Precio histórico (2014 - 2024)
- **Fuente:** Kaggle  
- **Enlace:** https://www.kaggle.com/datasets/kannapat/btc-usd-historical-price-2014-2024
---

## 🧩 Objetivos del Proyecto

### 1️⃣ Carga y Exploración de Datos
- Leer el archivo CSV utilizando `pandas`.
- Inspeccionar las primeras filas del dataset.
- Analizar tipos de datos y tamaño.
- Identificar valores nulos o columnas irrelevantes.

---

### 2️⃣ Limpieza y Preparación de Datos
- Convertir la columna de fechas al formato adecuado.
- Seleccionar únicamente las columnas relevantes.
- Tratar valores nulos de forma justificada.
- Establecer la fecha como índice temporal.

---

### 3️⃣ Análisis Estadístico Descriptivo
- Calcular estadísticas básicas:
  - Media
  - Máximo y mínimo
  - Rango
  - Desviación estándar
- Analizar la dispersión del precio y del volumen.
- Evaluar la relación entre precio de cierre y volumen.

---

### 4️⃣ Visualización de Datos
- Gráfica de línea del precio de cierre a lo largo del tiempo.
- Histograma de la distribución de precios de cierre.
- Gráfica de dispersión para analizar la correlación entre precio y volumen.

Las visualizaciones se realizan utilizando **matplotlib básico**.

---

### 5️⃣ Comunicación de Resultados
- Interpretar los resultados obtenidos.
- Redactar conclusiones claras:
  - Rango de precios observado.
  - Nivel de volatilidad.
  - Relación entre volumen y precio.
- Documentar los hallazgos en el notebook.

---

## 🧠 Conceptos Reforzados

| Área | Concepto | Aplicación práctica |
|----|----|----|
| Python | Manejo de archivos | Lectura de CSV |
| Pandas | DataFrames y estadísticas | `.describe()`, selección de columnas |
| NumPy | Operaciones numéricas | Cálculos estadísticos |
| Estadística | Medidas descriptivas | Media, desviación estándar |
| Visualización | Gráficos básicos | Series temporales, histogramas |
| Comunicación | Análisis e interpretación | Conclusiones escritas |

---

## 🛠 Herramientas Utilizadas

- Python
- pandas
- numpy
- matplotlib
- Jupyter Notebook

---

## 📁 Estructura del Proyecto

```text
cripto_analisis/
├── data/
│   └── BTC-USD (2014-2024).csv
├── notebooks/
│   └── analisis_exploratorio.ipynb
└── requirements.txt
