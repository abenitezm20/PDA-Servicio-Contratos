from dataclasses import dataclass
from contractual.seedwork.dominio.fabricas import Fabrica
from contractual.seedwork.dominio.repositorios import Repositorio
from contractual.modulos.contratos.dominio.repositorios import RepositorioPropiedadesContratos
from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioPropiedadesContratosSQL


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedadesContratos.__class__:
            return RepositorioPropiedadesContratosSQL()
        else:
            raise ExcepcionFabrica()
