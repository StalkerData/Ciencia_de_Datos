import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date


class DashboardView:
    def __init__(self, data_loader):
        """
        Recibe una instancia de WeatherDataAPI (Inyección de dependencias)
        """
        self.data_loader = data_loader

    def render(self):
        st.set_page_config(
            page_title="Cucuta Weather Dashboard", page_icon="🌤️", layout="wide"
        )

        # Obtención de datos
        try:
            df = self.data_loader.get_weather_data()
        except Exception as e:
            st.error(f"Error al cargar datos: {e}")
            return

        # Estado de la sesión para filtros
        if "active_metric" not in st.session_state:
            st.session_state.active_metric = "general"

        # Dibujar componentes
        self.__render_header()
        self.__render_kpis(df)

        st.divider()

        self.__render_selectors()

        # --- Configuración de métricas ---
        metric = st.session_state.active_metric
        config = self.__get_metric_config(metric)

        # --- Layout Dinámico ---
        # Si es "general", damos más espacio a la tabla (proporción 1.5 a 2)
        # Si es una métrica sola, mantenemos el espacio actual (1 a 2)
        if metric == "general":
            ratio = [1.6, 2]
        else:
            ratio = [1, 2]

        col_data, col_chart = st.columns(ratio)

        with col_data:
            with st.expander(
                "📋 Summary Statistics", expanded=True
            ):  # Cambiado a True para que se vea de una
                # Tip de experto: Redondea el describe para que no ocupe tanto espacio horizontal
                summary_df = df[config["cols"]].describe().round(2)
                st.dataframe(summary_df, use_container_width=True)

        with col_chart:
            fig = px.line(
                df,
                x="datetime",
                y=config["y"],
                title=config["title"],
                labels=config["labels"],
                template="plotly_dark",
            )  # O el que prefieras
            st.plotly_chart(fig, use_container_width=True)

        # Agregados Diarios
        st.subheader("Daily Aggregates")
        daily_df = self.data_loader.get_daily_aggregates()
        daily_cols = self.__get_daily_cols(metric)
        st.dataframe(daily_df[daily_cols], use_container_width=True)

    def __render_header(self):
        st.title("Cucuta Weather Dashboard — Last 7 Days 🚀")
        hoy = date.today()
        hace_7_dias = hoy - pd.to_timedelta(7, unit="D")
        st.markdown(
            f"""
            <div style="background-color: #e6f2ff; padding: 10px; border-radius: 5px;
                        border-left: 5px solid #1e90ff; margin: 10px 0; color: #000000;">
                <strong>📅 Date range: {hace_7_dias.strftime("%B %d, %Y")} to {hoy.strftime("%B %d, %Y")}</strong>
            </div>
        """,
            unsafe_allow_html=True,
        )

    def __render_kpis(self, df):
        ultimo = df.iloc[-1]
        penultimo = df.iloc[-2]
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        kpi1.metric(
            "🌡️ Temp",
            f"{ultimo['temperature']:.1f} °C",
            f"{ultimo['temperature'] - penultimo['temperature']:.1f} °C",
        )
        kpi2.metric(
            "💧 Humidity",
            f"{ultimo['humidity']:.1f} %",
            f"{ultimo['humidity'] - penultimo['humidity']:.1f} %",
        )
        kpi3.metric(
            "🌧️ Precip",
            f"{ultimo['precipitation']:.2f} mm",
            f"{ultimo['precipitation'] - penultimo['precipitation']:.2f} mm",
        )
        kpi4.metric(
            "🌦️ Rain",
            f"{ultimo['rain']:.2f} mm",
            f"{ultimo['rain'] - penultimo['rain']:.2f} mm",
        )

    def __render_selectors(self):
        cols = st.columns(5)
        metrics = [
            ("📊 General", "general"),
            ("🌡️ Temp", "temperature"),
            ("💧 Humidity", "humidity"),
            ("🌧️ Precip", "precipitation"),
            ("🌦️ Rain", "rain"),
        ]
        for i, (label, key) in enumerate(metrics):
            if cols[i].button(label):
                st.session_state.active_metric = key
        st.markdown(f"**Active filter:** `{st.session_state.active_metric.upper()}`")

    def __get_metric_config(self, metric):
        configs = {
            "general": {
                "cols": [
                    "datetime",
                    "temperature",
                    "humidity",
                    "precipitation",
                    "rain",
                ],
                "y": "temperature",
                "title": "Temperature (°C)",
                "labels": {"temperature": "Temperature (°C)", "datetime": "Date"},
            },
            "temperature": {
                "cols": ["datetime", "temperature"],
                "y": "temperature",
                "title": "Temperature (°C)",
                "labels": {"temperature": "Temperature (°C)", "datetime": "Date"},
            },
            "humidity": {
                "cols": ["datetime", "humidity"],
                "y": "humidity",
                "title": "Humidity (%)",
                "labels": {"humidity": "Humidity (%)", "datetime": "Date"},
            },
            "precipitation": {
                "cols": ["datetime", "precipitation"],
                "y": "precipitation",
                "title": "Precipitation (mm)",
                "labels": {"precipitation": "Precipitation (mm)", "datetime": "Date"},
            },
            "rain": {
                "cols": ["datetime", "rain"],
                "y": "rain",
                "title": "Rain (mm)",
                "labels": {"rain": "Rain (mm)", "datetime": "Date"},
            },
        }
        return configs[metric]

    def __get_daily_cols(self, metric):
        daily_configs = {
            "general": [
                "date",
                "temp_mean",
                "temp_min",
                "temp_max",
                "humidity_mean",
                "precipitation_total",
                "rain_total",
            ],
            "temperature": ["date", "temp_mean", "temp_min", "temp_max"],
            "humidity": ["date", "humidity_mean"],
            "precipitation": ["date", "precipitation_total"],
            "rain": ["date", "rain_total"],
        }
        return daily_configs[metric]
