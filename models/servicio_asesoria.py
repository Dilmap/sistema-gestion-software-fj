from exceptions.excepciones_personalizadas import DatoInvalidoError
from models.servicio import Servicio


class ServicioAsesoria(Servicio):
    """Asesoría especializada, cobrada por hora con recargo según el nivel."""

    NIVELES = {"basico": 0.0, "avanzado": 0.2, "experto": 0.5}

    def __init__(self, codigo: str, nombre: str, tarifa_base: float, nivel: str = "basico"):
        super().__init__(codigo, nombre, tarifa_base)
        self._nivel = self._validar_nivel(nivel)

    @property
    def nivel(self) -> str:
        return self._nivel

    def calcular_costo(self, horas: float, impuesto: float = 0.0, descuento: float = 0.0) -> float:
        horas = self._validar_horas(horas)
        impuesto = self._validar_porcentaje(impuesto, "impuesto")
        descuento = self._validar_porcentaje(descuento, "descuento")
        recargo = self.NIVELES[self._nivel]
        subtotal = self.tarifa_base * horas * (1 + recargo)
        total = subtotal * (1 + impuesto) * (1 - descuento)
        return round(total, 2)

    def describir(self) -> str:
        return f"Asesoría especializada {self._nombre} (código {self._identificador}, nivel {self._nivel})"

    def _validar_nivel(self, nivel):
        if nivel not in self.NIVELES:
            opciones = ", ".join(self.NIVELES)
            raise DatoInvalidoError(f"El nivel debe ser uno de: {opciones}.")
        return nivel

    @staticmethod
    def _validar_horas(horas):
        try:
            valor = float(horas)
        except (TypeError, ValueError):
            raise DatoInvalidoError("Las horas deben ser un número.")
        if valor <= 0:
            raise DatoInvalidoError("Las horas deben ser mayores que cero.")
        return valor

    @staticmethod
    def _validar_porcentaje(valor, nombre):
        try:
            porcentaje = float(valor)
        except (TypeError, ValueError):
            raise DatoInvalidoError(f"El {nombre} debe ser un número.")
        if not 0 <= porcentaje < 1:
            raise DatoInvalidoError(f"El {nombre} debe estar entre 0 y 1.")
        return porcentaje