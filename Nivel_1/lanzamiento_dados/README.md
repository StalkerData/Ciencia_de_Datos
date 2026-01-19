# 🎲 Simulador de Lanzamiento de Dados

## 📌 Descripción del Proyecto

Proyecto orientado a la **simulación computacional de experimentos aleatorios** usando dados de 6 caras.  
El objetivo no es jugar, sino practicar la **generación de números aleatorios**, el cálculo de frecuencias y la comparación entre **probabilidad teórica** y **probabilidad empírica** (simulaciones tipo Monte Carlo, en un nivel introductorio).

> Nota: El archivo `src/simulador.py` contiene la clase `Simulador`, que implementa la simulación utilizando `numpy.random.randint` para generar los lanzamientos.

---

## 🎯 Propósito

Demostrar comprensión práctica de conceptos fundamentales de probabilidad y estadística mediante la simulación de experimentos repetidos y el análisis de sus resultados.

---

## 🧠 Conocimientos y habilidades que demuestra

- Probabilidad teórica (eventos y espacio muestral).  
- Generación de números aleatorios con `numpy`.  
- Cálculo de frecuencias absolutas y relativas.  
- Comparación entre teoría y observación (empírica).  
- Estadística descriptiva básica (medidas y dispersión).  
- Visualización simple con `matplotlib` (gráficos de barras, histogramas).  

---

## 📦 Escenario del problema

Simular el lanzamiento de uno o varios dados N veces y analizar resultados como:

- Distribución de caras para 1 dado.
- Distribución de la suma para 2 dados.
- Convergencia de frecuencias empíricas hacia las probabilidades teóricas al aumentar N.

Ejemplos de experimentos:  
- 1 dado lanzado 10.000 veces.  
- 2 dados (suma) lanzados 50.000 veces.  

---

## 🧩 Objetivos del Proyecto

1. **Definir el experimento**
   - Elegir tipo de dado (6 caras).
   - Establecer número de lanzamientos N.
   - Decidir si se registra la cara de un solo dado o la suma de varios dados.

2. **Simulación computacional**
   - Generar resultados aleatorios repetidamente.
   - Almacenar resultados en estructuras apropiadas (listas, diccionarios de frecuencias).
   - Ejecutar el experimento para distintos valores de N.

3. **Cálculo de frecuencias y probabilidad empírica**
   - Calcular frecuencias absolutas (conteos).
   - Calcular frecuencias relativas (proporciones).
   - Derivar probabilidades empíricas a partir de las frecuencias relativas.

4. **Probabilidad teórica**
   - Formalizar la probabilidad teórica para cada evento:
     - Para 1 dado: probabilidad uniforme (1/6).
     - Para 2 dados: distribución de la suma (no uniforme).
   - Comparar la probabilidad teórica con la empírica obtenida por la simulación.

5. **Visualización e interpretación**
   - Graficar resultados (barras/histogramas) mostrando teoría vs simulación.
   - Analizar cómo varían las discrepancias al aumentar N.
   - Extraer conclusiones relacionadas con la Ley de los Grandes Números.

---

## 🛠 Herramientas utilizadas

- Python  
- NumPy (`numpy.random.randint`)  
- Matplotlib (visualización básica)  
- Jupyter Notebook (análisis interactivo)

---

## 📁 Estructura del proyecto

```text
lanzamiento_dados/
├── notebooks/
│   └── simulacion_dados.ipynb
├── results/
│   └── (gráficos y salidas)
├── src/
│   └── simulador.py   # contiene la clase Simulador que ejecuta la simulación
└── requirements.txt
