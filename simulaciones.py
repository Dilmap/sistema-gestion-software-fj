from exceptions.excepciones_personalizadas import SoftwareFJError
from models.cliente import Cliente
from models.reserva import Reserva
from models.servicio_asesoria import ServicioAsesoria
from models.servicio_equipos import ServicioEquipos
from models.servicio_salas import ServicioSalas
from utils.logger import configurar_logger

logger = configurar_logger()


def ejecutar_escenario(nombre, funcion):
    """Ejecuta un escenario sin dejar que un error detenga el programa."""
    logger.info(f"Inicio: {nombre}")
    try:
        resultado = funcion()
    except SoftwareFJError as error:
        logger.warning(f"{nombre}: error controlado: {error}")
        print(f"[{nombre}] Error controlado: {error}")
    except Exception as error:
        logger.error(f"{nombre}: error inesperado: {error}")
        print(f"[{nombre}] Error inesperado: {error}")
    else:
        logger.info(f"{nombre}: resultado {resultado}")
        print(f"[{nombre}] OK: {resultado}")
    finally:
        logger.info(f"Fin: {nombre}")


# ---------- Escenarios válidos ----------

def sim_01_cliente_valido():
    cliente = Cliente("12345678", "Ana Pérez", "ana@correo.com", "3001234567")
    return cliente.describir()


def sim_02_servicio_salas_valido():
    sala = ServicioSalas("SA1", "Sala Principal", 20000)
    return sala.calcular_costo(2)


def sim_03_equipos_con_impuesto_y_descuento():
    equipos = ServicioEquipos("EQ1", "Proyectores", 15000)
    return equipos.calcular_costo(3, cantidad=2, impuesto=0.19, descuento=0.1)


def sim_04_reserva_completa():
    cliente = Cliente("87654321", "Luis Gómez", "luis@correo.com")
    sala = ServicioSalas("SA2", "Sala Pequeña", 20000)
    reserva = Reserva(cliente, sala, 2, "R-004")
    reserva.confirmar()
    costo = reserva.procesar()
    return f"costo {costo}, estado {reserva.estado}"


# ---------- Escenarios con datos inválidos ----------

def sim_05_cliente_documento_invalido():
    return Cliente("abc123", "Juan Ruiz", "juan@correo.com")


def sim_06_cliente_correo_invalido():
    return Cliente("11223344", "Marta López", "correo-malo")


def sim_07_servicio_salas_horas_cero():
    sala = ServicioSalas("SA3", "Sala Grande", 20000)
    return sala.calcular_costo(0)


def sim_08_equipos_cantidad_invalida():
    equipos = ServicioEquipos("EQ2", "Portátiles", 15000)
    return equipos.calcular_costo(2, cantidad=0)


def sim_09_asesoria_nivel_invalido():
    return ServicioAsesoria("AS2", "Asesoría Contable", 50000, nivel="maestro")


def sim_10_procesar_sin_confirmar():
    cliente = Cliente("55667788", "Pedro Díaz", "pedro@correo.com")
    sala = ServicioSalas("SA4", "Sala Mediana", 20000)
    reserva = Reserva(cliente, sala, 1, "R-010")
    return reserva.procesar()


def sim_11_cancelar_reserva_procesada():
    cliente = Cliente("99887766", "Sara Mora", "sara@correo.com")
    sala = ServicioSalas("SA5", "Sala Ejecutiva", 20000)
    reserva = Reserva(cliente, sala, 1, "R-011")
    reserva.confirmar()
    reserva.procesar()
    reserva.cancelar()
    return reserva.estado


ESCENARIOS = [
    ("Cliente válido", sim_01_cliente_valido),
    ("Servicio salas válido", sim_02_servicio_salas_valido),
    ("Equipos con impuesto y descuento", sim_03_equipos_con_impuesto_y_descuento),
    ("Reserva completa", sim_04_reserva_completa),
    ("Cliente con documento inválido", sim_05_cliente_documento_invalido),
    ("Cliente con correo inválido", sim_06_cliente_correo_invalido),
    ("Salas con 0 horas", sim_07_servicio_salas_horas_cero),
    ("Equipos con cantidad 0", sim_08_equipos_cantidad_invalida),
    ("Asesoría con nivel inexistente", sim_09_asesoria_nivel_invalido),
    ("Procesar reserva sin confirmar", sim_10_procesar_sin_confirmar),
    ("Cancelar reserva procesada", sim_11_cancelar_reserva_procesada),
]


def ejecutar_todas():
    for nombre, funcion in ESCENARIOS:
        ejecutar_escenario(nombre, funcion)