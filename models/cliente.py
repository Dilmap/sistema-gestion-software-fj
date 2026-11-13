import re

from exceptions.excepciones_personalizadas import DatoInvalidoError
from models.entidad_abstracta import EntidadAbstracta
from utils.logger import configurar_logger

logger = configurar_logger()


class Cliente(EntidadAbstracta):
    """Cliente de Software FJ con datos personales encapsulados."""

    def __init__(self, documento, nombre, correo, telefono=""):
        try:
            super().__init__(self._validar_documento(documento))
            self.nombre = nombre
            self.correo = correo
            self.telefono = telefono
        except DatoInvalidoError as error:
            logger.warning(f"Cliente rechazado ({documento}): {error}")
            raise
        logger.info(f"Cliente creado: {self._identificador}")

    @staticmethod
    def _validar_documento(documento):
        texto = str(documento).strip()
        if not texto.isdigit() or not 5 <= len(texto) <= 15:
            raise DatoInvalidoError("El documento debe tener entre 5 y 15 dígitos.")
        return texto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(str(valor).strip()) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = str(valor).strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or not re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", str(valor).strip()):
            raise DatoInvalidoError("El correo no tiene un formato válido.")
        self._correo = str(valor).strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        texto = str(valor).strip() if valor else ""
        if texto and not re.fullmatch(r"\d{7,15}", texto):
            raise DatoInvalidoError("El teléfono debe tener entre 7 y 15 dígitos.")
        self._telefono = texto

    def describir(self) -> str:
        return f"Cliente {self._nombre} (documento {self._identificador})"