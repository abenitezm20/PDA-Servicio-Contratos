from __future__ import annotations
from dataclasses import dataclass
from contractual.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class PropiedadContratoRegistrado(EventoDominio):
    numero_contrato: str = None
    fecha_actualizacion: str = None
    fecha_creacion: str = None
    propiedad_id: str = None
