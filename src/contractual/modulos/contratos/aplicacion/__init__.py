from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion

from contractual.modulos.contratos.dominio.eventos import PropiedadContratoRegistrado

dispatcher.connect(HandlerReservaIntegracion.handle_contrato_creado,
                   signal=f'{PropiedadContratoRegistrado.__name__}Integracion')
