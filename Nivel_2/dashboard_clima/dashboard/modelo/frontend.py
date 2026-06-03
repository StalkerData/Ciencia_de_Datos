import streamlit as st
import pandas as pd
from datetime import date
#from recolector_datos import WeatherDataAPI
import plotly.express as px

#! para correr la app
# streamlit run  Nivel_2/dashboard_clima/dashboard/vista/frontend.py  --server.address=127.0.0.1 --browser.gatherUsageStats=false

st.set_page_config(
    page_title="Cucuta Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

# --- Data ---
datos_limpio = WeatherDataAPI()
dato = datos_limpio.get_weather_data()

# --- Session state para el botón activo ---
if "active_metric" not in st.session_state:
    st.session_state.active_metric = "general"

# --- Header ---
st.title("Cucuta Weather Dashboard — Last 7 Days 🚀")

hoy = date.today()
hace_7_dias = hoy - pd.to_timedelta(7, unit="D")

st.markdown(f"""
<div style="background-color: #e6f2ff; padding: 10px; border-radius: 5px;
            border-left: 5px solid #1e90ff; margin: 10px 0; color: #000000;">
    <strong>📅 Date range: {hace_7_dias.strftime("%m/%d/%Y")} to {hoy.strftime("%m/%d/%Y")}</strong>
</div>
""", unsafe_allow_html=True)

# --- Buttons ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("📊 General"):
        st.session_state.active_metric = "general"
with col2:
    if st.button("🌡️ Temperature"):
        st.session_state.active_metric = "temperature"
with col3:
    if st.button("💧 Humidity"):
        st.session_state.active_metric = "humidity"
with col4:
    if st.button("🌧️ Precipitation"):
        st.session_state.active_metric = "precipitation"
with col5:
    if st.button("🌦️ Rain"):
        st.session_state.active_metric = "rain"

# --- Lógica de filtrado según métrica activa ---
metric = st.session_state.active_metric

METRIC_CONFIG = {
    "general":       {"cols": ["datetime", "temperature", "humidity", "precipitation", "rain"], "y": "temperature",   "title": "Temperature (°C)"},
    "temperature":   {"cols": ["datetime", "temperature"],   "y": "temperature",   "title": "Temperature (°C)"},
    "humidity":      {"cols": ["datetime", "humidity"],      "y": "humidity",      "title": "Humidity (%)"},
    "precipitation": {"cols": ["datetime", "precipitation"], "y": "precipitation", "title": "Precipitation (mm)"},
    "rain":          {"cols": ["datetime", "rain"],          "y": "rain",          "title": "Rain (mm)"},
}

config = METRIC_CONFIG[metric]
df_display = dato[config["cols"]]

# --- Table + Chart ---
col_data, col_chart = st.columns(2)

with col_data:
    st.subheader("Summary Statistics")
    st.dataframe(df_display.describe())

with col_chart:
    fig = px.line(
        dato,
        x="datetime",
        y=config["y"],
        title=config["title"]
    )
    st.plotly_chart(fig, use_container_width=True)

# metricas:  date  temp_mean   temp_min   temp_max  humidity_mean  precipitation_total  rain_total
METRIC_CONFIG_DAILY={
    "general": ["date", "temp_mean", "temp_min", "temp_max", "humidity_mean", 'precipitation_total', 'rain_total'],
    "temperature": ["date", "temp_mean", "temp_min", "temp_max"],
    "humidity": ["date", "humidity_mean"],
    "precipitation": ["date",'precipitation_total'],
    "rain": ["date", 'rain_total'],
}
# --- Tabla de datos por de los 7 dias ---
st.dataframe(datos_limpio.get_daily_aggregates()[METRIC_CONFIG_DAILY[metric]])