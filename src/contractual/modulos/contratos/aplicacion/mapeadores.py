from contractual.seedwork.aplicacion.dto import Mapeador as AppMap
from contractual.seedwork.dominio.repositorios import Mapeador as RepMap
from contractual.modulos.contratos.aplicacion.dto import PropiedadContratoDTO
from contractual.modulos.contratos.dominio.entidades import PropiedadContrato


class MapeadorPropiedadContratosDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadContratoDTO:
        propiedad_dto = PropiedadContratoDTO
        propiedad_dto.fecha_actualizacion = externo.get('fecha_creacion')
        propiedad_dto.fecha_creacion = externo.get('fecha_actualizacion')
        propiedad_dto.numero_contrato = externo.get('numero_contrato')
        propiedad_dto.propiedad_id = externo.get('propiedad_id')
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadContratoDTO) -> dict:
        return dto.__dict__

    def obtener_tipo(self) -> type:
        return PropiedadContrato.__class__


class MapeadorPropiedadContrato(RepMap):
    def dto_a_entidad(self, dto: PropiedadContratoDTO) -> PropiedadContrato:
        entidad = PropiedadContrato()
        entidad.numero_contrato = dto.numero_contrato
        entidad.fecha_actualizacion = dto.fecha_actualizacion
        entidad.fecha_creacion = dto.fecha_creacion
        entidad.propiedad_id = dto.propiedad_id

        return entidad

    def entidad_a_dto(self, entidad: PropiedadContrato) -> PropiedadContratoDTO:
        dto = PropiedadContratoDTO(
            entidad.numero_contrato,
            entidad.fecha_creacion,
            entidad.fecha_actualizacion,
            entidad.propiedad_id,
        )
        return dto

    def obtener_tipo(self) -> type:
        return PropiedadContrato.__class__
