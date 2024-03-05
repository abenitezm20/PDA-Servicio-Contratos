from .entidades import PropiedadContrato
from .excepciones import TipoObjetoNoExisteEnDominioContratoExcepcion
from contractual.seedwork.dominio.repositorios import Mapeador
from contractual.seedwork.dominio.fabricas import Fabrica
from contractual.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaPropiedadContratos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad = mapeador.dto_a_entidad(obj)

            return propiedad


@dataclass
class FabricaPropiedadContratos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == PropiedadContrato.__class__:
            fabrica_propiedad = _FabricaPropiedadContratos()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioContratoExcepcion()
