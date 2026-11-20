from exceptions.excepciones_personalizadas import DatoInvalidoError
from models.servicio import Servicio


class ServicioEquipos(Servicio):
    """Alquiler de equipos, cobrado por hora y por cantidad de equipos."""

    def calcular_costo(
        self, horas: float, cantidad: int = 1, impuesto: float = 0.0, descuento: float = 0.0
    ) -> float:
        horas = self._validar_horas(horas)
        cantidad = self._validar_cantidad(cantidad)
        impuesto = self._validar_porcentaje(impuesto, "impuesto")
        descuento = self._validar_porcentaje(descuento, "descuento")
        subtotal = self.tarifa_base * horas * cantidad
        total = subtotal * (1 + impuesto) * (1 - descuento)
        return round(total, 2)

    def describir(self) -> str:
        return f"Alquiler de equipos {self._nombre} (código {self._identificador}, tarifa por equipo y hora {self._tarifa_base})"

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
    def _validar_cantidad(cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise DatoInvalidoError("La cantidad de equipos debe ser un entero mayor que cero.")
        return cantidad

    @staticmethod
    def _validar_porcentaje(valor, nombre):
        try:
            porcentaje = float(valor)
        except (TypeError, ValueError):
            raise DatoInvalidoError(f"El {nombre} debe ser un número.")
        if not 0 <= porcentaje < 1:
            raise DatoInvalidoError(f"El {nombre} debe estar entre 0 y 1.")
        return porcentaje