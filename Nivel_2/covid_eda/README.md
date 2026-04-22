# 🦠 Proyecto 2 — Análisis Exploratorio del COVID-19 (EDA)

**Nivel:** 2 — Manipulación y Análisis de Datos  
**Repositorio:** Ciencia_de_Datos  
**Autor:** StalkerData  

---

## 🎯 Propósito del Proyecto

El objetivo de este proyecto es realizar un **Análisis Exploratorio de Datos (EDA)** sobre un dataset real del COVID-19 a nivel mundial.

A diferencia de proyectos anteriores, este trabajo se enfoca en:

- Manejo de datos **grandes y desordenados**
- Limpieza de datos con valores faltantes
- Análisis temporal y comparativo
- Interpretación de datos reales

Este tipo de análisis es fundamental en roles de **Data Analyst y Data Scientist**.

---

## 📦 Dataset Utilizado

**Fuente:** Our World in Data (OWID)  
**Dataset:** COVID-19 global dataset  

https://covid.ourworldindata.org/data/owid-covid-data.csv

El dataset contiene información global sobre:

- Casos confirmados
- Muertes
- Población
- Indicadores sanitarios

Cada fila representa:

> 📅 Un país en una fecha específica

---

## 🧠 Enfoque del Análisis

Debido al tamaño y complejidad del dataset, se trabajó con un subconjunto de columnas relevantes:

- `location`
- `date`
- `total_cases`
- `new_cases`
- `total_deaths`
- `population`

Esto permite enfocarse en **análisis significativo sin ruido innecesario**.

---

## 🧩 Objetivos del Proyecto

El análisis busca responder preguntas clave:

- ¿Qué países tuvieron más casos de COVID-19?
- ¿Qué países registraron más muertes?
- ¿Cómo evolucionaron los casos a lo largo del tiempo?
- ¿Existen diferencias entre países al ajustar por población?

---

## 🔧 Herramientas Utilizadas

| Herramienta | Uso |
|------|------|
Python | Lenguaje principal |
Pandas | Limpieza y análisis de datos |
Matplotlib | Visualización |
Jupyter Notebook | Desarrollo del análisis |

---

## 🧪 Proceso de Análisis

El proyecto sigue un flujo típico de EDA:
```
Dataset (CSV)
↓
Carga con Pandas
↓
Exploración inicial
↓
Limpieza de datos (valores nulos, tipos)
↓
Selección de columnas relevantes
↓
Transformación de datos
↓
Análisis por país
↓
Análisis temporal
↓
Visualización
↓
Interpretación de resultados
```

---

## 📊 Análisis Realizados

### 1️⃣ Exploración del dataset
- Identificación de columnas relevantes
- Análisis de valores nulos
- Revisión de tipos de datos

### 2️⃣ Limpieza de datos
- Manejo de valores faltantes
- Conversión de fechas a formato `datetime`
- Filtrado de datos relevantes

### 3️⃣ Análisis por país
- Comparación de casos totales
- Comparación de muertes

### 4️⃣ Análisis temporal
- Evolución de casos a lo largo del tiempo
- Identificación de tendencias y picos

### 5️⃣ Normalización de datos
- Casos en relación a la población
- Comparación más justa entre países

---

## 📈 Visualizaciones

Se utilizaron:

- 📈 Gráficos de líneas → evolución temporal
- 📊 Gráficos de barras → comparación entre países

El enfoque está en **interpretar los datos**, no solo en graficarlos.

---

## 📁 Estructura del Proyecto

```
covid_eda/
├── data
│ └── owid-covid-data.csv
├── notebooks
│ └── analisis_covid.ipynb
├── requirements.txt
└── results
```


---

## 📦 Dependencias

```
ipykernel==7.0.0
pandas==2.3.3
matplotlib==3.10.7
requests==2.32.5
```

Instalación:

```bash
pip install -r requirements.txt
```

## 📌 Resultados del Análisis

El análisis permite:

- Identificar los países más afectados
- Comprender la evolución global de la pandemia
- Comparar el impacto relativo entre países
- Detectar patrones en el comportamiento del virus

## ⚠️ Consideraciones
El dataset contiene valores faltantes importantes
No todos los países tienen datos completos
El análisis depende de decisiones de limpieza y filtrado

## 👤 Autor

**[StalkerData](https://github.com/StalkerData)**

---

Regresar al **[Principal](../../README.md) 🏠**

