from contractual.seedwork.aplicacion.queries import Query, QueryResultado
from contractual.seedwork.aplicacion.queries import ejecutar_query as query
from contractual.modulos.contratos.infraestructura.repositorios import RepositorioPropiedadesContratosSQL
from dataclasses import dataclass
from .base import PropiedadContratosQueryBaseHandler
from contractual.modulos.contratos.aplicacion.mapeadores import MapeadorPropiedadContrato


@dataclass
class ObtenerPropiedadContratos(Query):
    id: str


class ObtenerPropiedadContratosHandler(PropiedadContratosQueryBaseHandler):

    def handle(self, query: ObtenerPropiedadContratos) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedadesContratosSQL.__class__)
        propiedad_contratos = self.fabrica_propiedad_contratos.crear_objeto(
            repositorio.obtener_por_id(query.id), MapeadorPropiedadContrato())
        return QueryResultado(resultado=propiedad_contratos)


@query.register(ObtenerPropiedadContratos)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedadContratos):
    handler = ObtenerPropiedadContratosHandler()
    return handler.handle(query)


@dataclass
class ObtenerContratos(Query):
    pass


class ObtenerContratosHandler(PropiedadContratosQueryBaseHandler):

    def handle(self, query: Query) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedadesContratosSQL.__class__)
        tmp = repositorio.obtener_todos()
        resultado = []
        for i in tmp:
            resultado.append(self.fabrica_propiedad_contratos.crear_objeto(
                i, MapeadorPropiedadContrato()))
        return QueryResultado(resultado=resultado)


@query.register(Query)
def ejecutar_query_obtener_contratos(query: Query):
    handler = ObtenerContratosHandler()
    return handler.handle(query)
