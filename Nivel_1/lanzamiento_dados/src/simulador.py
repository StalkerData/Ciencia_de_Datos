import numpy as np


class Simulador:
    """
    Clase que permite simular lanzamientos de dados.
    """

    @classmethod
    def dados(cls, caras_dado, cantidad_dados=1):
        """
        Configura el tipo de dado y la cantidad de dados a utilizar.

        Parameters
        ----------
        caras_dado : int
            Número de caras que tiene el dado.
        cantidad_dados : int, optional
            Cantidad de dados a lanzar en cada experimento (por defecto 1).
        """
        cls.caras_dado = caras_dado
        cls.cantidad_dados = cantidad_dados

    @classmethod
    def lanzamientos(cls, cantidad_lanzamientos=1000000):
        """
        Realiza múltiples lanzamientos de los dados configurados.

        Parameters
        ----------
        cantidad_lanzamientos : int, optional
            Número de lanzamientos a simular (por defecto 1.000.000).

        Returns
        -------
        numpy.ndarray
            Arreglo con los resultados de los lanzamientos.
            Cada fila representa un lanzamiento y cada columna un dado.
        """
        return np.random.randint(
            1, cls.caras_dado + 1, size=(cantidad_lanzamientos, cls.cantidad_dados)
        )
