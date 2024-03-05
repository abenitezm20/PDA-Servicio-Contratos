from contractual.seedwork.aplicacion.comandos import ComandoHandler
from contractual.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from contractual.modulos.contratos.dominio.fabricas import FabricaPropiedadContratos


class RegistrarPropiedadContratosBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedad: FabricaPropiedadContratos = FabricaPropiedadContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad
