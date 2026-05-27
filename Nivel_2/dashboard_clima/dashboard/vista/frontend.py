import streamlit as st
import pandas as pd
from datetime import date

# para correr la app
# streamlit run  Nivel_2/dashboard_clima/dashboard/vista/frontend.py  --server.address=127.0.0.1 --browser.gatherUsageStats=false

st.title("Dashboard del Clima de Cúcuta en los últimos 7 Días 🚀")

hoy = date.today()
hace_7_dias = hoy - pd.to_timedelta(7, unit="D")
hoy_str = hoy.strftime("%d/%m/%Y")
hace_7_dias_str = hace_7_dias.strftime("%d/%m/%Y")

formato = f"""
<div style="background-color: #e6f2ff; padding: 10px; border-radius: 5px; border-left: 5px solid #1e90ff; margin: 10px 0; color: #000000;">
    <strong>📅 Rango de fechas: {hace_7_dias_str} a {hoy_str}</strong>
</div>
"""
st.markdown(formato, unsafe_allow_html=True)

# Crear 4 columnas para los botones
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("temperature_2m"):
        st.write("temperature_2m")

with col2:
    if st.button("relative_humidity_2m"):
        st.write("relative_humidity_2m")

with col3:
    if st.button("precipitation"):
        st.write("precipitation")

with col4:
    if st.button("rain"):
        st.write("rain")
