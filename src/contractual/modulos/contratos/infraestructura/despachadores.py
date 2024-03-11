import pulsar
from pulsar.schema import *

from contractual.modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado, ContratoCreadoPayload
from contractual.modulos.contratos.infraestructura.schema.v1.comandos import ComandoCrearContratoFallido, ComandoCrearContratoFallidoPayload
from contractual.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schemas):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schemas)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ContratoCreadoPayload(
            id_propiedad=str(evento.id_propiedad),
            numero_contrato=str(evento.numero_contrato),
        )
        evento_integracion = EventoContratoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoContratoCreado))

    def publicar_comando(self, dto, topico):
        payload = ComandoCrearContratoFallidoPayload(
            id_propiedad=dto.propiedad_id,
            numero_contrato=dto.numero_contrato,
        )

        comando_integracion = ComandoCrearContratoFallido(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoCrearContratoFallido))
