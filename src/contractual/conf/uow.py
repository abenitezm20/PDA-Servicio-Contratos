from contractual.conf.db import db_session as db
from contractual.seedwork.infraestructura.uow import UnidadTrabajo, Batch
from pydispatch import dispatcher

import logging
import traceback


class ExcepcionUoW(Exception):
    ...


class UnidadTrabajoSQLAlchemy(UnidadTrabajo):

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnidadTrabajo:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _limpiar_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return list[db.get_nested_transaction()]

    @property
    def batches(self) -> list[Batch]:
        return self._batches

    def commit(self):
        print('Commit unidad de trabajo SQLALCHEMY, Ejecutando commit a BD')
        for batch in self.batches:
            lock = batch.lock
            batch.operacion(*batch.args, **batch.kwargs)

        db.commit()  # Commits the transaction

        super().commit()

    def rollback(self, savepoint=None):
        if savepoint:
            savepoint.rollback()
        else:
            db.rollback()

        super().rollback()

    def savepoint(self):
        db.begin_nested()


class UnidadTrabajoPulsar(UnidadTrabajo):

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnidadTrabajo:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _limpiar_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return []

    @property
    def batches(self) -> list[Batch]:
        return self._batches

    def commit(self):
        print('Commit unidad de trabajo PULSAR, Publicando eventos')
        index = 0
        try:
            for evento in self._obtener_eventos():
                dispatcher.send(
                    signal=f'{type(evento).__name__}Integracion', evento=evento)
                index += 1
        except:
            logging.error('ERROR: Suscribiendose al tópico de eventos!')
            traceback.print_exc()
            self.rollback(index=index)
        self._limpiar_batches()

    def rollback(self, index=None):
        # TODO Implemente la función de rollback
        # Vea los métodos agregar_evento de la clase AgregacionRaiz
        # A cada evento que se agrega, se le asigna un evento de compensación
        # Piense como podría hacer la implementación

        super().rollback()

    def savepoint(self):
        # NOTE No hay punto de implementar este método debido a la naturaleza de Event Sourcing
        ...