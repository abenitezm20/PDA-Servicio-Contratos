from __future__ import annotations
from dataclasses import dataclass, field
from contractual.seedwork.dominio.entidades import AgregacionRaiz
from contractual.modulos.contratos.dominio.eventos import PropiedadContratoRegistrado


@dataclass
class PropiedadContrato(AgregacionRaiz):
    propiedad_id: str = field(default=str)
    numero_contrato: str = field(default=str)
    fecha_creacion: str = field(default=str)
    fecha_actualizacion: str = field(default=str)

    def registrar_propiedad(self, propiedad: PropiedadContrato):

        self.agregar_evento(PropiedadContratoRegistrado(
            propiedad_id=propiedad.propiedad_id,
            numero_contrato=propiedad.numero_contrato,
            fecha_creacion=propiedad.fecha_creacion,
            fecha_actualizacion=propiedad.fecha_actualizacion))
