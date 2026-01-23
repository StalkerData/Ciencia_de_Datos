# 🎓 Sistema de Gestión de Notas Académicas usando Diccionarios

---

## 📌 Descripción del Proyecto

Este proyecto implementa un sistema sencillo de gestión y análisis de notas académicas utilizando **diccionarios anidados en Python**.

El objetivo principal es demostrar el **dominio del pensamiento algorítmico** y el manejo de colecciones básicas, sin utilizar bases de datos ni librerías avanzadas, apoyándose únicamente en estructuras nativas del lenguaje.

El proyecto forma parte del **Nivel 1 – Fundamentos de Programación para Ciencia de Datos**.

---

## 🧠 Propósito del Proyecto

Representar, manipular y analizar información académica estructurada (estudiantes, materias y notas) utilizando:

- Diccionarios anidados
- Bucles y condicionales
- Operaciones aritméticas básicas
- Archivos JSON para persistencia de datos

Este tipo de ejercicio refleja situaciones reales donde se requiere **modelar datos estructurados sin infraestructura compleja**.

---

## 🎯 Objetivo General

Construir un sistema que permita:

- Registrar estudiantes y sus calificaciones.
- Almacenar la información en estructuras de datos en memoria.
- Analizar el rendimiento académico mediante estadísticas simples.
- Mostrar resultados claros y ordenados.

---

## 🧩 Objetivos Específicos

### 🔹 Objetivo 1 – Representación de los Datos

Diseñar una estructura de datos que represente:

- Un conjunto de estudiantes.
- Cada estudiante con:
  - Nombre
  - Edad
  - Materias y notas asociadas

La información se almacena en un **diccionario principal**, donde cada clave identifica a un estudiante y su valor es otro diccionario con los detalles académicos.

Esto demuestra el uso correcto de **diccionarios anidados** para modelar relaciones jerárquicas.

---

### 🔹 Objetivo 2 – Ingreso y Gestión de Datos

Permitir:

- Generar estudiantes de forma automática.
- Agregar nuevos estudiantes manualmente.
- Editar el diccionario de estudiantes en memoria.

Para ello se utilizan dos componentes principales:

#### 📄 `GeneradorEstudiantes.py`
Contiene la clase `GeneradorEstudiantes`, cuya función es:

- Crear datos sintéticos de estudiantes.
- Asignar nombres, edades y notas aleatorias.
- Guardar la información generada en un archivo `.json` dentro de la carpeta `data/`.

Este archivo permite contar con un dataset inicial para análisis.

#### 📄 `ManagerEstudiante.py`
Contiene la clase `ManagerEstudiante`, encargada de:

- Cargar el diccionario desde el archivo JSON.
- Manipular los datos en memoria.
- Agregar nuevos estudiantes con validaciones.
- Gestionar la estructura del diccionario de estudiantes.

---

### 🔹 Objetivo 3 – Cálculo de Estadísticas Simples

A partir de los datos registrados, se calculan:

- Promedio de notas por estudiante.
- Promedio de notas por materia.
- Mejor y peor nota por materia.
- Ordenamiento de estudiantes según su promedio general.

Este paso refuerza el uso de:

- Bucles `for`
- Operaciones aritméticas
- Comprensiones de listas
- Funciones auxiliares

---

### 🔹 Objetivo 4 – Capa Básica de Análisis

Como parte del análisis adicional, se realizan tareas como:

- Ordenar estudiantes por rendimiento académico.
- Identificar mejores y peores desempeños.
- Obtener resúmenes generales del grupo.

Este análisis introduce lógica condicional y ordenamiento con `sorted()`.

---

### 🔹 Objetivo 5 – Presentación de Resultados

Los resultados se muestran de forma clara mediante:

- Impresión formateada en consola o notebook.
- Resúmenes por estudiante y por materia.
- Listados ordenados por promedio.

El enfoque está en la **claridad del resultado**, no en la visualización avanzada.

---

## 📘 Conceptos Clave Reforzados

| Concepto | Descripción |
|--------|-------------|
| Diccionarios anidados | Estructura central del sistema |
| Bucles `for` | Recorrido de estudiantes y materias |
| Condicionales `if` | Validaciones y lógica académica |
| Comprensiones de listas | Extracción y procesamiento de datos |
| Estadística básica | Promedios, máximos y mínimos |
| Archivos JSON | Persistencia simple de datos |

---

## 🛠 Herramientas Utilizadas

- Python
- Diccionarios y listas
- JSON
- Jupyter Notebook

---

## 📁 Estructura del Proyecto

```
gestion_notas_diccionarios/
├── data/
│   └── estudiantes.json
├── notebooks/
│   └── gestion_de_notas.ipynb
├── src/
│   ├── GeneradorEstudiantes.py
│   └── ManagerEstudiante.py
└── requirements.txt
```
