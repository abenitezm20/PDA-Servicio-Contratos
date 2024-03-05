from pulsar.schema import *
from contractual.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class RegistroArrendamientoPayload(Record):
    propiedad_id = String()
    numero_contrato = String()
    fecha_actualizacion = String()
    fecha_creacion = String()


class EventoRegistroArrendamientoCreado(EventoIntegracion):
    data = RegistroArrendamientoPayload()
