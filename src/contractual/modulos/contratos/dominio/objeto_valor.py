from enum import Enum

class EstadoPropiedad(str, Enum):
    EN_VALIDACION = 'en_validación'
    APROBADA = 'aprobada'
    RECHAZADA = 'rechazada'