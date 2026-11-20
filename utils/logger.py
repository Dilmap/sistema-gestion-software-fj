import logging
import os

RUTA_LOG = os.path.join("logs", "app.log")


def configurar_logger(nombre: str = "software_fj") -> logging.Logger:
    """Configura y devuelve el logger único del sistema."""
    logger = logging.getLogger(nombre)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)
    os.makedirs(os.path.dirname(RUTA_LOG), exist_ok=True)

    manejador = logging.FileHandler(RUTA_LOG, encoding="utf-8")
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    manejador.setFormatter(formato)
    logger.addHandler(manejador)
    return logger