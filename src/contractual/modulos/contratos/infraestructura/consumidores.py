import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback
from contractual.modulos.contratos.infraestructura.proyecciones import ProyeccionRegistrarArrendamiento
from contractual.modulos.contratos.infraestructura.schema.v1.eventos import EventoRegistroArrendamientoCreado
from contractual.modulos.contratos.infraestructura.schema.v1.comandos import ComandoRegistrarArrendamiento
from contractual.seedwork.infraestructura import utils
from contractual.modulos.contratos.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from contractual.seedwork.infraestructura.proyecciones import ejecutar_proyeccion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contrato', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-eventos', schema=AvroSchema(EventoRegistroArrendamientoCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-contrato', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoRegistrarArrendamiento))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            print(mensaje.value().data.numero_contrato)
            ejecutar_proyeccion(ProyeccionRegistrarArrendamiento(
                ProyeccionRegistrarArrendamiento.ADD,
                mensaje.value().data.propiedad_id,
                mensaje.value().data.numero_contrato,
                mensaje.value().data.fecha_creacion,
                mensaje.value().data.fecha_actualizacion
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
