from contractual.modulos.contratos.dominio.repositorios import RepositorioPropiedadesContratos
from contractual.modulos.contratos.dominio.fabricas import FabricaPropiedadContratos
from contractual.modulos.contratos.dominio.entidades import PropiedadContrato
from contractual.conf.db import db_session
from uuid import UUID
from .dto import PropiedadContrato as PropiedadContratoDTO
from .mapeadores import MapeadorPropiedadContratos


class RepositorioPropiedadesContratosSQL(RepositorioPropiedadesContratos):

    def __init__(self):
        self._fabrica_propiedad_contratos: FabricaPropiedadContratos = FabricaPropiedadContratos()

    @property
    def fabrica_propiedad_contratos(self):
        return self._fabrica_propiedad_contratos

    def obtener_por_id(self, id: UUID) -> PropiedadContrato:
        reserva_dto = db_session.query(
            PropiedadContratoDTO).filter_by(propiedad_id=str(id)).one()
        return self._fabrica_propiedad_contratos.crear_objeto(reserva_dto, MapeadorPropiedadContratos())

    def obtener_todos(self) -> list[PropiedadContrato]:
        ...

    def agregar(self, propiedad: PropiedadContrato):
        propiedad_dto = self._fabrica_propiedad_contratos.crear_objeto(
            propiedad, MapeadorPropiedadContratos())
        db_session.add(propiedad_dto)

    def actualizar(self, propiedad: PropiedadContrato):
        ...

    def eliminar(self, propiedad_id: UUID):
        print(f'Eliminando propiedad con id: {propiedad_id}')
        contrato = db_session.query(
            PropiedadContratoDTO).filter_by(propiedad_id=str(propiedad_id)).one()
        db_session.delete(contrato)
