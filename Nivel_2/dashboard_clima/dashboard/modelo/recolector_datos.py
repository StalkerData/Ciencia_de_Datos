import logging

import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

logger = logging.getLogger(__name__)


class WeatherDataAPI:
    """
    Recolector de datos meteorológicos horarios desde Open-Meteo.
    Cubre los últimos 7 días para la ubicación configurada.
    """

    DEFAULT_LATITUDE = 7.9
    DEFAULT_LONGITUDE = -72.5
    DEFAULT_TIMEZONE = "America/Bogota"
    CACHE_TTL = 3600  # segundos

    def __init__(
        self, latitude: float = DEFAULT_LATITUDE, longitude: float = DEFAULT_LONGITUDE
    ):
        self.__url = "https://api.open-meteo.com/v1/forecast"
        self.__params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": [
                "temperature_2m",
                "relative_humidity_2m",
                "precipitation",
                "rain",
            ],
            "timezone": self.DEFAULT_TIMEZONE,
            "past_days": 7,
            "forecast_days": 1,  # mínimo 1 para evitar respuestas vacías
        }
        cache_session = requests_cache.CachedSession(
            ".cache", expire_after=self.CACHE_TTL
        )
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        self.__client = openmeteo_requests.Client(session=retry_session)
        self.__df: pd.DataFrame | None = None
        logger.info(
            "Cliente WeatherDataAPI inicializado (lat=%s, lon=%s)", latitude, longitude
        )

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def is_loaded(self) -> bool:
        return self.__df is not None and not self.__df.empty

    # ------------------------------------------------------------------
    # Métodos públicos
    # ------------------------------------------------------------------

    def get_weather_data(self, force_refresh: bool = False) -> pd.DataFrame:
        """
        Obtiene y retorna los datos horarios del clima.

        Args:
            force_refresh: Si True, ignora el caché interno y vuelve a llamar la API.

        Returns:
            DataFrame con columnas: datetime, temperature, humidity, precipitation, rain.

        Raises:
            RuntimeError: Si la API no devuelve datos válidos.
        """
        if self.is_loaded and not force_refresh:
            return self.__df.copy()

        try:
            responses = self.__client.weather_api(self.__url, params=self.__params)
        except Exception as e:
            raise RuntimeError(f"Error al conectarse con Open-Meteo: {e}") from e

        response = responses[0]
        hourly = response.Hourly()

        df = self.__parse_hourly(hourly)
        self.__validate_dataframe(df)

        df["datetime"] = df["datetime"].dt.tz_convert(self.DEFAULT_TIMEZONE)
        self.__df = df

        logger.info(
            "Datos obtenidos: %.4f°N %.4f°E — %d registros",
            response.Latitude(),
            response.Longitude(),
            len(df),
        )
        return self.__df.copy()

    def get_summary(self) -> pd.DataFrame:
        """
        Retorna estadísticas descriptivas de las variables numéricas.
        Llama a get_weather_data() solo si aún no hay datos cargados.
        """
        if not self.is_loaded:
            self.get_weather_data()
        return self.__df.describe()

    def get_daily_aggregates(self) -> pd.DataFrame:
        """
        Retorna agregados diarios: temp promedio/min/max, precipitación total,
        humedad promedio. Útil para gráficas de resumen en el dashboard.
        """
        if not self.is_loaded:
            self.get_weather_data()

        df = self.__df.copy()
        df["date"] = df["datetime"].dt.date

        return (
            df.groupby("date")
            .agg(
                temp_mean=("temperature", "mean"),
                temp_min=("temperature", "min"),
                temp_max=("temperature", "max"),
                humidity_mean=("humidity", "mean"),
                precipitation_total=("precipitation", "sum"),
                rain_total=("rain", "sum"),
            )
            .round(2)
            .reset_index()
        )

    # ------------------------------------------------------------------
    # Métodos privados
    # ------------------------------------------------------------------

    @staticmethod
    def __parse_hourly(hourly) -> pd.DataFrame:
        """Convierte la respuesta horaria de Open-Meteo a DataFrame."""
        return pd.DataFrame(
            {
                "datetime": pd.date_range(
                    start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                    end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                    freq=pd.Timedelta(seconds=hourly.Interval()),
                    inclusive="left",
                ),
                "temperature": hourly.Variables(0).ValuesAsNumpy(),
                "humidity": hourly.Variables(1).ValuesAsNumpy(),
                "precipitation": hourly.Variables(2).ValuesAsNumpy(),
                "rain": hourly.Variables(3).ValuesAsNumpy(),
            }
        )

    @staticmethod
    def __validate_dataframe(df: pd.DataFrame) -> None:
        """Valida que el DataFrame tenga datos utilizables."""
        if df.empty:
            raise RuntimeError("La API devolvió un DataFrame vacío.")

        numeric_cols = ["temperature", "humidity", "precipitation", "rain"]
        all_nan_cols = [col for col in numeric_cols if df[col].isna().all()]
        if all_nan_cols:
            raise RuntimeError(
                f"Las siguientes columnas están completamente vacías: {all_nan_cols}"
            )
