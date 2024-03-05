from contractual.seedwork.dominio.repositorios import Mapeador
from contractual.modulos.contratos.dominio.entidades import PropiedadContrato
from .dto import PropiedadContrato as PropiedadContratoDTO


class MapeadorPropiedadContratos(Mapeador):

    def obtener_tipo(self) -> type:
        return PropiedadContrato.__class__

    def entidad_a_dto(self, entidad: PropiedadContrato) -> PropiedadContratoDTO:
        propiedad_dto = PropiedadContratoDTO(
            entidad.propiedad_id,
            entidad.numero_contrato,
            entidad.fecha_creacion,
            entidad.fecha_actualizacion
        )

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadContratoDTO) -> PropiedadContrato:
        propiedad = PropiedadContrato(
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            numero_contrato=dto.numero_contrato,
            propiedad_id=dto.propiedad_id,
        )

        return propiedad
