import json
import random


class GeneradorEstudiantes:
    def __init__(self):
        # Listas de nombres, segundos nombres, apellidos y materias
        self.nombres = [
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
        self.segundos_nombres = [
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
        self.apellidos = [
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
        self.materias = ["Matemáticas", "Inglés", "Programación", "Estadística"]

    def generar_estudiante(self, id_estudiante):
        # Generar nombre completo
        nombre = random.choice(self.nombres)
        segundo_nombre = random.choice(self.segundos_nombres)
        apellido = random.choice(self.apellidos)
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"

        # Generar edad aleatoria entre 18 y 30
        edad = random.randint(18, 30)

        # Generar notas aleatorias para cada materia
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

    def generar_estudiantes(self, cantidad, ruta_archivo):
        estudiantes = {}
        for i in range(1, cantidad + 1):
            id_estudiante = f"2023{str(i).zfill(3)}"
            estudiante = self.generar_estudiante(id_estudiante)
            estudiantes.update(estudiante)

        # Guardar el resultado en un archivo JSON
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)

        return estudiantes
