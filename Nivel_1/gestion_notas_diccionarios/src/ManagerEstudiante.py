from typing import Dict, Any, Union


class ManagerEstudiante:
    """
    Gestor de estado y operaciones para estudiantes.

    Esta clase actúa como un controlador que mantiene el registro de estudiantes
    en memoria (a nivel de clase) y proporciona métodos interactivos para
    la captura y validación de datos por consola.

    Attributes:
        _estudiantes (Dict[str, Any]): Diccionario "privado" que almacena
            la base de datos de estudiantes en memoria.
    """

    _estudiantes: Dict[str, Any] = {}

    @classmethod
    def estudiantes(cls) -> Dict[str, Any]:
        """
        Obtiene una copia segura del registro actual de estudiantes.

        Returns:
            Dict[str, Any]: Una copia del diccionario de estudiantes para evitar
            modificaciones accidentales directas sobre la referencia original.
        """
        return cls._estudiantes.copy()

    @classmethod
    def estudiantes_set(cls, estudiantes: Dict[str, Any]) -> None:
        """
        Sobrescribe el registro completo de estudiantes.

        Args:
            estudiantes (Dict[str, Any]): El nuevo diccionario de estudiantes
                que reemplazará al actual.
        """
        cls._estudiantes = estudiantes

    @classmethod
    def agregar_estudiante(
        cls, codigo: str, nombre: str, edad: int, materias: Dict[str, float]
    ) -> None:
        """
        Agrega o actualiza un estudiante en el registro interno.

        Args:
            codigo (str): Identificador único del estudiante.
            nombre (str): Nombre completo.
            edad (int): Edad validada.
            materias (Dict[str, float]): Diccionario de materias y sus notas.
        """
        cls._estudiantes[codigo] = {
            "nombre": nombre,
            "edad": edad,
            "materias": materias,
        }

    @staticmethod
    def _ingresar_entero(mensaje: str) -> int:
        """
        Solicita un número entero al usuario de forma robusta.

        Mantiene un bucle infinito hasta que el usuario ingresa un valor válido,
        manejando excepciones de tipo ValueError.

        Args:
            mensaje (str): El texto a mostrar en el prompt.

        Returns:
            int: El número entero ingresado por el usuario.
        """
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print("⚠️  Error: Por favor, ingrese un número entero válido.")

    @staticmethod
    def _ingresar_flotantes(mensaje: str) -> float:
        """
        Solicita un número decimal (float) al usuario de forma robusta.

        Args:
            mensaje (str): El texto a mostrar en el prompt.

        Returns:
            float: El número decimal ingresado.
        """
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("⚠️  Error: Por favor, ingrese un número válido (ej. 4.5).")

    @classmethod
    def _crear_nota(cls) -> float:
        """
        Solicita y valida una nota académica.

        Utiliza `_ingresar_flotantes` y verifica que el valor esté
        dentro del rango permitido [0.0, 5.0].

        Returns:
            float: Una nota válida entre 0.0 y 5.0.
        """
        while True:
            nota = cls._ingresar_flotantes("Ingrese la nota del estudiante: ")
            if 0.0 <= nota <= 5.0:
                return nota
            print("❌ La nota debe estar entre 0.0 y 5.0. Intente nuevamente.")

    @classmethod
    def _edad_valida(cls) -> int:
        """
        Solicita y valida la edad del estudiante.

        Utiliza `_ingresar_entero` y verifica un rango lógico [5, 100].

        Returns:
            int: Una edad válida.
        """
        while True:
            edad = cls._ingresar_entero("Ingrese la edad del estudiante: ")
            if 5 <= edad <= 100:
                return edad
            print("❌ La edad debe estar entre 5 y 100 años. Intente nuevamente.")

    @classmethod
    def crear_estudiante(cls) -> None:
        """
        Flujo interactivo principal para crear un nuevo estudiante.

        Guía al usuario paso a paso para:
        1. Ingresar un código único (verifica duplicados).
        2. Ingresar datos personales.
        3. Ingresar notas para materias predefinidas.
        4. Guardar el estudiante en el registro de la clase.
        """
        print("\n--- Creación de Nuevo Estudiante ---")
        while True:
            codigo = input("Ingrese el código del estudiante: ")
            if codigo in cls._estudiantes:
                print(f"⚠️  El código '{codigo}' ya existe. Intente con otro.")
                continue

            nombre = input("Ingrese el nombre del estudiante: ")
            edad = cls._edad_valida()

            materias = {}
            # Lista de materias hardcodeada para el ejemplo interactivo
            lista_materias = ["Matemáticas", "Inglés", "Programación", "Estadística"]

            print(f"Ingrese las notas para {nombre}:")
            for materia in lista_materias:
                print(f" > Materia: {materia}")
                nota = cls._crear_nota()
                materias[materia] = nota

            cls.agregar_estudiante(codigo, nombre, edad, materias)
            print(f"✅ Estudiante {nombre} (ID: {codigo}) agregado correctamente.")
            break
