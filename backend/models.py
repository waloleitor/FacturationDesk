from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Enum
from sqlalchemy.orm import declarative_base
import enum

Base= declarative_base()

#Metodo de cobro como enum para validacion
class MetodoCobro(enum.Enum):
    tarjeta = "tarjeta"
    efectivo = "efectivo"
    transferencia = "transferencia"
    otros = "otros"

class Factura(Base):
    __tablename__ = "facturas"


    id=Column(Integer, primary_key=True, autoincrement=True)
    fecha_factura = Column(Date, nullable=False)
    numero_factura = Column(String, nullable=False, unique=True)
    cliente = Column(String, nullable=False)
    ruta = Column(String)
    precio = Column(Float)
    pdf_path = Column(String)

    cobrada = Column(Boolean, default=False)
    rechazada = Column(Boolean, default=False)
    metodo_cobro = Column(Enum(MetodoCobro), nullable=True)
    fecha_cobro = Column(Date, nullable=True)

    entregada_ppcr = Column(Boolean, default=False)
    fecha_entrega = Column(Date, nullable=True)
    
    creada_por = Column(String, nullable=False) #para guardar quien la creó