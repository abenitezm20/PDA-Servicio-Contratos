import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback
import uuid
from datetime import datetime
from contractual.modulos.contratos.infraestructura.proyecciones import ProyeccionRegistrarArrendamiento
from contractual.modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado
from contractual.modulos.contratos.infraestructura.schema.v1.comandos import ComandoRegistrarArrendamiento, ComandoCrearContratoFallido
from contractual.seedwork.infraestructura import utils
from contractual.modulos.contratos.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from contractual.seedwork.infraestructura.proyecciones import ejecutar_proyeccion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contratro-creado', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-eventos', schema=AvroSchema(EventoContratoCreado))

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
        consumidor = cliente.subscribe('comandos-crear-contrato', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoRegistrarArrendamiento))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionRegistrarArrendamiento(
                ProyeccionRegistrarArrendamiento.ADD,
                mensaje.value().data.id_propiedad,
                uuid.uuid4(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_compensacion(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-crear-contrato-fallido', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearContratoFallido))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando compensacion recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionRegistrarArrendamiento(
                ProyeccionRegistrarArrendamiento.DELETE,
                mensaje.value().data.id_propiedad,
                uuid.uuid4(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
