from exceptions.excepciones_personalizadas import (
    DatoInvalidoError,
    OperacionNoPermitidaError,
    ReservaInvalidaError,
)
from models.cliente import Cliente
from models.entidad_abstracta import EntidadAbstracta
from models.servicio import Servicio
from utils.logger import configurar_logger

logger = configurar_logger()


class Reserva(EntidadAbstracta):
    """Reserva que une un cliente, un servicio y una duración, con estados controlados."""

    def __init__(self, cliente, servicio, duracion, codigo):
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("La reserva requiere un cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("La reserva requiere un servicio válido.")
        super().__init__(str(codigo).strip())
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = self._validar_duracion(duracion)
        self._estado = "pendiente"
        logger.info(f"Reserva {self._identificador} creada para {cliente.identificador}")

    @property
    def estado(self) -> str:
        return self._estado

    def confirmar(self):
        if self._estado != "pendiente":
            self._registrar_no_permitida("confirmar")
        self._estado = "confirmada"
        logger.info(f"Reserva {self._identificador} confirmada")

    def cancelar(self):
        if self._estado in ("procesada", "cancelada"):
            self._registrar_no_permitida("cancelar")
        self._estado = "cancelada"
        logger.info(f"Reserva {self._identificador} cancelada")

    def procesar(self) -> float:
        if self._estado != "confirmada":
            self._registrar_no_permitida("procesar")
        try:
            costo = self._servicio.calcular_costo(self._duracion)
        except DatoInvalidoError as error:
            logger.error(f"Reserva {self._identificador}: error al calcular costo: {error}")
            raise ReservaInvalidaError(
                f"No se pudo calcular el costo de la reserva {self._identificador}."
            ) from error
        self._estado = "procesada"
        logger.info(f"Reserva {self._identificador} procesada por {costo}")
        return costo

    def describir(self) -> str:
        return (
            f"Reserva {self._identificador}: {self._cliente.nombre} - "
            f"{self._servicio.nombre} ({self._duracion} h, {self._estado})"
        )

    @staticmethod
    def _validar_duracion(duracion):
        try:
            valor = float(duracion)
        except (TypeError, ValueError):
            raise DatoInvalidoError("La duración debe ser un número.")
        if valor <= 0:
            raise DatoInvalidoError("La duración debe ser mayor que cero.")
        return valor

    def _registrar_no_permitida(self, accion):
        mensaje = f"No se puede {accion} una reserva en estado {self._estado}."
        logger.warning(f"Reserva {self._identificador}: {mensaje}")
        raise OperacionNoPermitidaError(mensaje)