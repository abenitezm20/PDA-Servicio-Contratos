from contractual.modulos.contratos.aplicacion.mapeadores import MapeadorPropiedadContratosDTOJson
from contractual.modulos.contratos.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from contractual.modulos.contratos.infraestructura.despachadores import Despachador
from contractual.seedwork.aplicacion.comandos import ejecutar_comando
from contractual.seedwork.aplicacion.handlers import Handler
from datetime import datetime


class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_contrato_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contrato')


class HandlePropiedadDominio():
    @staticmethod
    def handle_propiedad_registrada(evento):
        obj = {
            "fecha_creacion": datetime.now(),
            "fecha_actualizacion": datetime.now(),
            "propiedad_id": evento.propiedad_id,
            "numero_contrato": evento.numero_contrato
        }
        map_propiedad = MapeadorPropiedadContratosDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(obj)
        comando = RegistrarPropiedadContratos(
            propiedad_dto.numero_contrato,
            propiedad_dto.fecha_actualizacion,
            propiedad_dto.fecha_creacion,
            propiedad_dto.propiedad_id
        )

        ejecutar_comando(comando)
