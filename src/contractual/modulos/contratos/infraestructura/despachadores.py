import pulsar
from pulsar.schema import *

from contractual.modulos.contratos.infraestructura.schema.v1.eventos import EventoRegistroArrendamientoCreado, RegistroArrendamientoPayload
from contractual.modulos.contratos.infraestructura.schema.v1.comandos import ComandoRegistrarArrendamiento, ComandoRegistrarArrendamientoPayload
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
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = RegistroArrendamientoPayload(
            propiedad_id=str(evento.propiedad_id),
            numero_contrato=str(evento.numero_contrato),
            fecha_actualizacion=str(evento.fecha_actualizacion),
            fecha_creacion=str(evento.fecha_creacion),
        )
        evento_integracion = EventoRegistroArrendamientoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoRegistroArrendamientoCreado))

    def publicar_comando(self, dto, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        # if isinstance(comando, ComandoRegistrarArrendamiento):
        #     print('AQUI :)')

        payload = ComandoRegistrarArrendamientoPayload(
            propiedad_id=dto.propiedad_id,
            numero_contrato=dto.numero_contrato,
            fecha_actualizacion=dto.fecha_actualizacion,
            fecha_creacion=dto.fecha_creacion,
        )

        comando_integracion = ComandoRegistrarArrendamiento(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoRegistrarArrendamiento))
