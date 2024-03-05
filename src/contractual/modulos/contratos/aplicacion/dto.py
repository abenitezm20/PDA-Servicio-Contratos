from dataclasses import dataclass, field
from contractual.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadContratoDTO(DTO):
    numero_contrato: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
