from abc import ABC
from contractual.seedwork.dominio.repositorios import Repositorio


class RepositorioPropiedadesContratos(Repositorio, ABC):
    ...


class RepositorioProveedores(Repositorio, ABC):
    ...
