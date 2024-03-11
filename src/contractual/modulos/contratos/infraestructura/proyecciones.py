from contractual.modulos.contratos.dominio.entidades import PropiedadContrato
from contractual.modulos.contratos.dominio.eventos import PropiedadContratoRegistrado
from contractual.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from contractual.modulos.contratos.infraestructura.repositorios import RepositorioPropiedadesContratosSQL
from contractual.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from contractual.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from contractual.modulos.contratos.infraestructura.despachadores import Despachador
from abc import ABC, abstractmethod
import traceback
import time


class ProyeccionArrendamiento(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...


class ProyeccionRegistrarArrendamiento(ProyeccionArrendamiento):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, operacion, propiedad_id, numero_contrato, fecha_creacion, fecha_actualizacion):
        self.operacion = operacion
        self.propiedad_id = propiedad_id
        self.numero_contrato = numero_contrato
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion

    def ejecutar(self, db=None):
        if not db:
            print('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(
            RepositorioPropiedadesContratosSQL.__class__)

        if self.operacion == self.DELETE:
            print('Ejecutando proyección compensación de arrendamiento...')
            repositorio.eliminar(self.propiedad_id)
            db.commit()
            return

        print('Ejecutando proyección de arrendamiento...')
        time.sleep(5)
        
        repositorio.agregar(
            PropiedadContrato(propiedad_id=self.propiedad_id,
                              numero_contrato=self.numero_contrato,
                              fecha_creacion=self.fecha_creacion,
                              fecha_actualizacion=self.fecha_actualizacion))
        db.commit()

        evento = PropiedadContratoRegistrado(id_propiedad=self.propiedad_id,
                                             numero_contrato=self.numero_contrato,)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contratro-creado')
        print('Proyección de arrendamiento ejecutada!')


class ProyeccionReservaHandler(ProyeccionHandler):

    def handle(self, proyeccion: ProyeccionArrendamiento):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from contractual.conf.db import db_session as db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionRegistrarArrendamiento)
def ejecutar_proyeccion_arriendo(proyeccion, app=None):
    if not app:
        print('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionReservaHandler()
            handler.handle(proyeccion)

    except:
        traceback.print_exc()
        print('ERROR: Persistiendo!')
