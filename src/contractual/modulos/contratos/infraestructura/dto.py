from contractual.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer


class PropiedadContrato(Base):
    __tablename__ = "propiedades_contratos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    propiedad_id = Column(String)
    numero_contrato = Column(String)
    fecha_creacion = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    def __init__(self, propiedad_id, numero_contrato, fecha_creacion, fecha_actualizacion):
        self.propiedad_id = propiedad_id
        self.numero_contrato = numero_contrato
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
