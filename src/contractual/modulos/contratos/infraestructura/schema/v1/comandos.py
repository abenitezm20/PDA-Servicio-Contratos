from pulsar.schema import *
from dataclasses import dataclass, field
from contractual.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearContratoPayload(Record):
    id_propiedad = String()

class ComandoRegistrarArrendamiento(ComandoIntegracion):
    data = ComandoCrearContratoPayload()

class ComandoCrearContratoFallidoPayload(Record):
    id_propiedad = String()

class ComandoCrearContratoFallido(ComandoIntegracion):
    data = ComandoCrearContratoFallidoPayload()