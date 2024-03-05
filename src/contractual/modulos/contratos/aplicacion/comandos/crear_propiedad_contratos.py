from dataclasses import dataclass
from contractual.seedwork.aplicacion.comandos import Comando
from contractual.seedwork.aplicacion.comandos import ejecutar_comando as comando
from contractual.modulos.contratos.aplicacion.dto import PropiedadContratoDTO
from contractual.modulos.contratos.dominio.entidades import PropiedadContrato
from contractual.modulos.contratos.aplicacion.mapeadores import MapeadorPropiedadContrato
from contractual.modulos.contratos.infraestructura.repositorios import RepositorioPropiedadesContratosSQL
from contractual.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .base import RegistrarPropiedadContratosBaseHandler


@dataclass
class RegistrarPropiedadContratos(Comando):
    numero_contrato: str
    fecha_actualizacion: str
    fecha_creacion: str
    propiedad_id: str


class RegistrarPropiedadContratosHandler(RegistrarPropiedadContratosBaseHandler):

    def handle(self, comando: RegistrarPropiedadContratos):
        propiedad_dto = PropiedadContratoDTO(
            numero_contrato=comando.numero_contrato,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            propiedad_id=comando.propiedad_id,
        )

        propiedad: PropiedadContrato = self.fabrica_propiedad.crear_objeto(
            propiedad_dto, MapeadorPropiedadContrato())
        propiedad.registrar_propiedad(propiedad)
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedadesContratosSQL.__class__)

        print('Registrando crear contrato en la unidad de trabajo')
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()


@comando.register(RegistrarPropiedadContratos)
def ejecutar_comando_crear_reserva(comando: RegistrarPropiedadContratos):
    print('Registrando comando crear contrato')
    handler = RegistrarPropiedadContratosHandler()
    handler.handle(comando)
