from contractual.seedwork.aplicacion.queries import QueryHandler
from contractual.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from contractual.modulos.contratos.dominio.fabricas import FabricaPropiedadContratos


class PropiedadContratosQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedad_contratos: FabricaPropiedadContratos = FabricaPropiedadContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedad_contratos(self):
        return self._fabrica_propiedad_contratos
