from contractual.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioContratoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de contratos'):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
