from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base

#crear el motor de la base de datos SQLite
engine = create_engine("sqlite:///facturas-db", echo=True) #echo=True para ver Logs SQL

#crear la sesion (Puente entre Python y la base de datos)
SessionLocal = sessionmaker(bind=engine)

#Crear las tablas en la base de datos(si no existen)
def crear_base_de_datos():
    Base.metadata.create_all(engine)