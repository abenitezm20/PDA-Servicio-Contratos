from flask import Blueprint, Response, request, session
from contractual.modulos.contratos.aplicacion.queries.obtener_contratos import ObtenerPropiedadContratos
from contractual.modulos.contratos.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from contractual.modulos.contratos.aplicacion.mapeadores import MapeadorPropiedadContratosDTOJson
from contractual.seedwork.aplicacion.queries import ejecutar_query
from contractual.seedwork.aplicacion.comandos import ejecutar_comando

from contractual.modulos.contratos.infraestructura.despachadores import Despachador
from contractual.modulos.contratos.infraestructura.schema.v1.comandos import ComandoCrearContratoFallido


ab = Blueprint('contratos', __name__)


@ab.route('/contratos/health', methods=['GET'])
def health():
    return Response({'result': 'OK'}, status=200, mimetype='application/json')


@ab.route('/contratos/propiedad/<id>', methods=['GET'])
def obtener_propiedad_contratro(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedadContratos(id))
        map_propiedad = MapeadorPropiedadContratosDTOJson()
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return Response({'message': 'GET'})


@ab.route('/contrato', methods=['POST'])
def registrar_propiedad_contratro():
    session['uow_metodo'] = 'db'
    propiedad_dict = request.json
    map_propiedad = MapeadorPropiedadContratosDTOJson()
    propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
    comando = RegistrarPropiedadContratos(
        propiedad_dto.numero_contrato,
        propiedad_dto.fecha_actualizacion,
        propiedad_dto.fecha_creacion,
        propiedad_dto.propiedad_id,
    )

    print('Comando crear contrato inicio')
    ejecutar_comando(comando)
    print('Comando crear contrato fin')

    return Response('{}', status=202, mimetype='application/json')


@ab.route('/async-contrato', methods=['POST'])
def registrar_propiedad_contratro_async():
    map_propiedad = MapeadorPropiedadContratosDTOJson()
    arriendo_dto = map_propiedad.externo_a_dto(request.json)
    Despachador().publicar_comando(arriendo_dto, 'comandos-contrato')
    return Response('{}', status=202, mimetype='application/json')
