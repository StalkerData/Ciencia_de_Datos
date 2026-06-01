import streamlit as st
import pandas as pd
from datetime import date
#from recolector_datos import WeatherDataAPI
import plotly.express as px

# ✅ SIEMPRE el primero
st.set_page_config(
    page_title="Dashboard Clima Cúcuta",
    page_icon="🌤️",
    layout="wide"
)

# --- Datos ---
datos_limpio = WeatherDataAPI()
dato = datos_limpio.get_weather_data()

# --- Encabezado ---
st.title("Dashboard del Clima de Cúcuta en los últimos 7 Días 🚀")

hoy = date.today()
hace_7_dias = hoy - pd.to_timedelta(7, unit="D")
hoy_str = hoy.strftime("%d/%m/%Y")
hace_7_dias_str = hace_7_dias.strftime("%d/%m/%Y")

formato = f"""
<div style="background-color: #e6f2ff; padding: 10px; border-radius: 5px;
            border-left: 5px solid #1e90ff; margin: 10px 0; color: #000000;">
    <strong>📅 Rango de fechas: {hace_7_dias_str} a {hoy_str}</strong>
</div>
"""
st.markdown(formato, unsafe_allow_html=True)

# --- Botones ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🌡️ Temperatura"):
        st.write("temperature")
with col2:
    if st.button("💧 Humedad"):
        st.write("humidity")
with col3:
    if st.button("🌧️ Precipitación"):
        st.write("precipitation")
with col4:
    if st.button("🌦️ Lluvia"):
        st.write("rain")

# --- Tabla y gráfica ---
col_datos, col_grafico = st.columns(2)

with col_datos:
    st.dataframe(dato.describe())

with col_grafico:
    fig = px.line(
        dato,
        x='datetime',        # ✅ nombre real de la columna
        y='temperature',     # ✅ nombre real de la columna
        title='Temperatura (°C)'
    )
    st.plotly_chart(fig, use_container_width=True)