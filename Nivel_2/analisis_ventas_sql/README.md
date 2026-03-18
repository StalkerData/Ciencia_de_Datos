# 📊 Proyecto 1 — Análisis de Ventas con SQL + Pandas

**Nivel:** 2 — Manipulación y Análisis de Datos  
**Repositorio:** Ciencia_de_Datos  
**Autor:** StalkerData  

---

## 🎯 Propósito del Proyecto

El objetivo de este proyecto es analizar un conjunto de **datos reales de ventas** utilizando Python, Pandas y consultas SQL.

Este ejercicio busca demostrar la capacidad de:

- Cargar y explorar datasets reales.
- Limpiar y preparar datos para análisis.
- Utilizar SQL como herramienta analítica.
- Integrar consultas SQL con Pandas.
- Interpretar resultados mediante visualización y conclusiones.

Este tipo de análisis es común en roles de **Data Analyst y Data Scientist junior**.

---

## 📦 Dataset Utilizado

**Dataset:** Online Retail (2010–2011)  
**Fuente:** UCI Machine Learning Repository  

https://archive.ics.uci.edu/dataset/352/online+retail

El dataset contiene transacciones de una tienda minorista online con información como:

- Número de factura
- Código de producto
- Descripción del producto
- Cantidad vendida
- Precio unitario
- Fecha de compra
- Identificador del cliente
- País del cliente

Cada fila representa **una línea de venta dentro de una factura**.

---

## 🧠 Objetivos del Proyecto

El análisis busca responder preguntas clave sobre el comportamiento de las ventas:

- ¿Cuál es el **ingreso total generado**?
- ¿Qué **país genera más ventas**?
- ¿Cuál es el **producto más vendido**?
- ¿Cómo **evolucionan las ventas en el tiempo**?
- ¿Qué **cliente realiza más compras**?

Estas preguntas representan análisis típicos de negocio en datasets transaccionales.

---

## 🔧 Herramientas Utilizadas

| Herramienta | Uso |
|------|------|
Python | Lenguaje principal de análisis |
Pandas | Manipulación y preparación de datos |
DuckDB | Ejecución de consultas SQL analíticas |
Matplotlib | Visualización de resultados |
Jupyter Notebook | Desarrollo del análisis |

---

## 🧩 Flujo de Trabajo

El proyecto sigue un flujo típico de análisis de datos:
```
analisis_ventas_sql/
├── data
├── notebooks
│ └── analisis_ventas.ipynb
├── requirements.txt
└── results
```


### 📂 data
Contiene el dataset original utilizado en el análisis.

### 📓 notebooks
Notebook principal donde se realiza todo el análisis del proyecto.

### 📊 results
Carpeta destinada a almacenar gráficos o resultados exportados.

### 📦 requirements.txt
Listado de dependencias necesarias para ejecutar el proyecto.

---

## 🧾 Dependencias

Las librerías necesarias para ejecutar el proyecto son:
```
pandas=2.3.3
duckdb=1.4.4
matplotlib=3.10.7
openpyxl=3.1.5
requests=2.32.5
jinja2=3.1.6
```
Se pueden instalar con:
```
pip install -r requirements.txt
```

## 👤 Autor

**StalkerData**

Repositorio personal de aprendizaje y desarrollo en **Ciencia de Datos con Python**.
