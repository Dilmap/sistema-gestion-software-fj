from abc import abstractmethod

from exceptions.excepciones_personalizadas import DatoInvalidoError, ParametroFaltanteError
from models.entidad_abstracta import EntidadAbstracta


class Servicio(EntidadAbstracta):
    """Clase abstracta para los servicios que ofrece Software FJ."""

    def __init__(self, codigo: str, nombre: str, tarifa_base: float):
        if not codigo or not str(codigo).strip():
            raise ParametroFaltanteError("El código del servicio es obligatorio.")
        super().__init__(str(codigo).strip())
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(str(valor).strip()) < 3:
            raise DatoInvalidoError("El nombre del servicio debe tener al menos 3 caracteres.")
        self._nombre = str(valor).strip()

    @property
    def tarifa_base(self) -> float:
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        try:
            tarifa = float(valor)
        except (TypeError, ValueError):
            raise DatoInvalidoError("La tarifa base debe ser un número.")
        if tarifa <= 0:
            raise DatoInvalidoError("La tarifa base debe ser mayor que cero.")
        self._tarifa_base = tarifa

    @abstractmethod
    def calcular_costo(self, horas: float) -> float:
        """Calcula el costo del servicio para una cantidad de horas."""

    def describir(self) -> str:
        return f"Servicio {self._nombre} (código {self._identificador}, tarifa base {self._tarifa_base})"

    