class ManagerEstudiante:
    _estudiantes = {}

    @classmethod
    def estudiantes(cls):
        return cls._estudiantes.copy()
    
    @classmethod
    def estudiantes_set(cls, estudiantes):
        cls._estudiantes = estudiantes

    # funcion para agregar estuciante
    @classmethod
    def agregar_estudiante(cls, codigo, nombre, edad, materias):
        cls._estudiantes[codigo] = {"nombre": nombre, "edad": edad, "materias": materias}

    # funcion para ingrasar enteros
    @staticmethod
    def _ingresar_entero(mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    # funcion para ingrasar flotantes
    @staticmethod
    def _ingresar_flotantes(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("Por favor, ingrese un número válido.")

    # funcion para crea una nota entre 0 y 5
    @classmethod
    def _crear_nota(cls):
        while True:
            nota = cls._ingresar_flotantes("Ingrese la nota del estudiante: ")
            if nota < 0 or nota > 5:
                print("La nota debe estar entre 0 y 5. Intente nuevamente.")
                continue
            return nota

    # funcion para crear edad valida
    @classmethod
    def _edad_valida(cls):
        while True:
            edad = cls._ingresar_entero("Ingrese la edad del estudiante: ")
            if edad < 5 or edad > 100:
                print("La edad debe estar entre 5 y 100 años. Intente nuevamente.")
                continue
            return edad

    # funcion crear estudiante
    @classmethod
    def crear_estudiante(cls):
        while True:
            codigo = input("Ingrese el código del estudiante: ")
            if codigo in cls._estudiantes:
                print("El código ya existe. Intente con otro.")
                continue
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = cls._edad_valida()
            materias = {}
            for materia in ["Matemáticas", "Inglés", "Programación", "Estadística"]:
                nota = cls._crear_nota()
                materias[materia] = nota
            cls.agregar_estudiante(codigo, nombre, edad, materias)
            print(f"Estudiante {nombre} agregado correctamente.")
            break