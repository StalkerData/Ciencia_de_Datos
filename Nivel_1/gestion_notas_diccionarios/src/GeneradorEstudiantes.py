import json
import random
from typing import Dict, List, Any


class GeneradorEstudiantes:
    """
    Clase utilitaria para generar datos sintéticos de estudiantes.

    Esta clase permite crear perfiles de estudiantes con nombres, edades
    y calificaciones aleatorias en materias predefinidas, y exportar
    los resultados a un archivo JSON.

    Attributes:
        nombres (List[str]): Lista de primeros nombres disponibles.
        segundos_nombres (List[str]): Lista de segundos nombres disponibles.
        apellidos (List[str]): Lista de apellidos disponibles.
        materias (List[str]): Lista de materias para generar notas.
    """

    def __init__(self) -> None:
        """Inicializa las listas de datos base para la generación aleatoria."""
        self.nombres: List[str] = [
            "Juan",
            "Ana",
            "Luis",
            "María",
            "Carlos",
            "Laura",
            "Pedro",
            "Sofía",
            "Andrés",
            "Valentina",
            "Jorge",
            "Isabella",
            "Diego",
            "Gabriela",
            "Alejandro",
        ]
        self.segundos_nombres: List[str] = [
            "David",
            "María",
            "Fernando",
            "Alejandra",
            "Andrés",
            "Valentina",
            "José",
            "Carolina",
            "Felipe",
            "Natalia",
            "Ricardo",
            "Daniela",
            "Javier",
            "Paula",
            "Sebastián",
        ]
        self.apellidos: List[str] = [
            "Pérez",
            "Gómez",
            "Castro",
            "Ruiz",
            "López",
            "García",
            "Martínez",
            "Rodríguez",
            "Sánchez",
            "Díaz",
            "Hernández",
            "Álvarez",
            "Moreno",
            "Jiménez",
            "Torres",
        ]
        self.materias: List[str] = [
            "Matemáticas",
            "Inglés",
            "Programación",
            "Estadística",
        ]

    def generar_estudiante(self, id_estudiante: str) -> Dict[str, Dict[str, Any]]:
        """
        Genera los datos de un solo estudiante con valores aleatorios.

        Combina nombres y apellidos, asigna una edad entre 18 y 30 años,
        y genera calificaciones flotantes (1.0 - 5.0) para las materias.

        Args:
            id_estudiante (str): El identificador único del estudiante (ej. "2023001").

        Returns:
            Dict[str, Dict[str, Any]]: Un diccionario con la estructura:
            {
                id_estudiante: {
                    "nombre": str,
                    "edad": int,
                    "materias": Dict[str, float]
                }
            }
        """
        # Generar nombre completo
        nombre = random.choice(self.nombres)
        segundo_nombre = random.choice(self.segundos_nombres)
        apellido = random.choice(self.apellidos)
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"

        # Generar edad aleatoria entre 18 y 30
        edad = random.randint(18, 30)

        # Generar notas aleatorias para cada materia (redondeadas a 1 decimal)
        materias_notas = {
            materia: round(random.uniform(1.0, 5.0), 1) for materia in self.materias
        }

        return {
            id_estudiante: {
                "nombre": nombre_completo,
                "edad": edad,
                "materias": materias_notas,
            }
        }

    def generar_estudiantes(self, cantidad: int, ruta_archivo: str) -> Dict[str, Any]:
        """
        Genera una lista masiva de estudiantes y la guarda en un archivo JSON.

        Genera IDs secuenciales con el formato '2023xxx'.

        Args:
            cantidad (int): El número total de estudiantes a generar.
            ruta_archivo (str): La ruta o nombre del archivo donde se guardará el JSON.

        Returns:
            Dict[str, Any]: El diccionario completo de todos los estudiantes generados.

        Raises:
            IOError: Si hay problemas al escribir el archivo en disco.
        """
        estudiantes = {}

        for i in range(1, cantidad + 1):
            # Genera ID con padding de ceros (ej. 1 -> "2023001")
            id_estudiante = f"2023{str(i).zfill(3)}"
            estudiante = self.generar_estudiante(id_estudiante)
            estudiantes.update(estudiante)

        # Guardar el resultado en un archivo JSON
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")
            # Opcional: re-lanzar la excepción si quieres manejarla arriba
            raise

        return estudiantes
