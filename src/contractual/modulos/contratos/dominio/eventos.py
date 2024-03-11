from __future__ import annotations
from dataclasses import dataclass
from contractual.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class PropiedadContratoRegistrado(EventoDominio):
    id_propiedad: str = None
    numero_contrato: str = None

@dataclass
class PropiedadContratoReversado(EventoDominio):
    id_propiedad: str = None
