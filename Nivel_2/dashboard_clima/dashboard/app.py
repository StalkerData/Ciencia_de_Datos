#! run app
# streamlit run  dashboard/app.py  --server.address=127.0.0.1 --browser.gatherUsageStats=false
# streamlit run  Nivel_2/dashboard_clima/dashboard/app.py  --server.address=127.0.0.1 --browser.gatherUsageStats=false
import sys
import os

# Añadir el directorio raíz al path para que las importaciones funcionen
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo.recolector_datos import WeatherDataAPI
from vista.frontend import DashboardView


def main():
    # 1. Inicializar el modelo (Lógica de datos)
    # Puedes pasar latitud y longitud personalizadas aquí
    recolector = WeatherDataAPI(latitude=7.9, longitude=-72.5)

    # 2. Inicializar la vista (Interfaz)
    # Le pasamos el recolector para que la vista pueda pedir datos
    dashboard = DashboardView(recolector)

    # 3. Ejecutar el renderizado
    dashboard.render()


if __name__ == "__main__":
    main()
