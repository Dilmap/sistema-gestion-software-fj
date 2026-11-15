from abc import ABC, abstractmethod


class EntidadAbstracta(ABC):
    """Clase base abstracta para las entidades del sistema."""

    def __init__(self, identificador: str):
        self._identificador = identificador

    @property
    def identificador(self) -> str:
        return self._identificador

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción legible de la entidad."""