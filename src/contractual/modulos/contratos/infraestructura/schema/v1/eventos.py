from pulsar.schema import *
from contractual.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class ContratoCreadoPayload(Record):
    id_propiedad = String()
    numero_contrato = String()


class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()
