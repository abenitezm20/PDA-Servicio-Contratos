from pulsar.schema import *
from dataclasses import dataclass, field
from contractual.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoRegistrarArrendamientoPayload(Record):
    propiedad_id = String()
    numero_contrato = String()
    fecha_actualizacion = String()
    fecha_creacion = String()


class ComandoRegistrarArrendamiento(ComandoIntegracion):
    data = ComandoRegistrarArrendamientoPayload()
