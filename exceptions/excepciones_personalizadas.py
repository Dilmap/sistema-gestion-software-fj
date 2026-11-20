class SoftwareFJError(Exception):
    """Excepción base del sistema Software FJ."""


class DatoInvalidoError(SoftwareFJError):
    """Se lanza cuando un dato no cumple las validaciones."""


class ParametroFaltanteError(SoftwareFJError):
    """Se lanza cuando falta un parámetro obligatorio."""


class OperacionNoPermitidaError(SoftwareFJError):
    """Se lanza cuando una operación no está permitida en el estado actual."""


class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio no está disponible."""


class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando una reserva no puede crearse o procesarse."""


class CalculoInconsistenteError(SoftwareFJError):
    """Se lanza cuando un cálculo produce un resultado inconsistente."""